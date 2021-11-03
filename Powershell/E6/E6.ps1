#√ÅngelaMontoyaAldape,IanIsraelLeijaMedina,DarielaHurtadoTorres
#https://www.ainur.es/blog/eliminar-red-wifi-por-comandos-en-windows/
#https://www.solvetic.com/tutoriales/article/8415-comando-activar-desactivar-wifi-windows-10-cmd/
#https://www.cybernautas.es/como-ver-todas-las-contrasenas-wifi-almacenadas-en-windows-10/

#Este codigo utilizara funciones para poder mostrar la contraseÒa, apagar, encender y borrar una red wifi
#Se recomiendo utilizar de antemano el comando "netsh wlan show profiles" para saber el nombre de su red

$i = $true
while ($i -eq ($true)){
    $op = Read-Host -prompt "øQuÈ opciÛn desea realizar?`n[1] Mostrar ContraseÒas`n[2] Prender/Apagar wifi`n[3] Borrar red`n[4] Salir"
    switch($op){
        1{ 
            show-passwd
        }2{
            on-off
        }3{
            delete
        }4{
            exit
        }default{
            Write-Host "Ingreso un valor inv·lido"
        }
    }
}