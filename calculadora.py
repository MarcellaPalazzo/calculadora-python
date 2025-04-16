print("Calculadora Simples")

while True:
  num1 = float(input("Digite o primeiro número: "))
  operador = input("Digite o operador (+, -, *, /, ^): ")
  num2 = float(input("Digite o segundo número: "))

  if operador == "+":
      resultado = num1 + num2
  elif operador == "-":
      resultado = num1 - num2
  elif operador == "*":
      resultado = num1 * num2   
  elif operador == "/":
      if num2 != 0:
          resultado = num1 / num2
      else:
          resultado = "Erro! Divisão por zero."
  elif operador == "^":
      resultado = num1 ** num2        
  else:
      resultado = "Operador inválido."

  if isinstance(resultado, (int, float)):
      print("Resultado: ", round(resultado, 1))
  else:
      print("Resultado: ", resultado)    

  continuar = input("Deseja realizar outra operação? (s/n): ").lower()
  if continuar != "s":
      print("Encerrando a calculadora. Até a próxima!") 
      break   

                      
        
