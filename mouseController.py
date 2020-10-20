from pynput.mouse import Button, Controller
mouse = Controller()
#print(mouse.position) #Da um print na posição atual do mouse
mouse.position = (111, 757) #Coloca o mouse em uma posição especifica
#mouse.move() #Movimenta o mouse nas posições especificadas
mouse.click(Button.left, 1)#Faz com que clique em um botão do mouse Left Right Middle sendo o numero a quantidade de click
#mouse.press(Button.left) #Preciona e segura o botão
#mouse.release(Button.left) #Faz com que o botão pare de ser precionado
#mouse.scroll(0, -100) #Move o scroll de paginas




