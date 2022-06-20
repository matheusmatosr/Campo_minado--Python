def exibe():
  print('-------Campo minado versão python--------')
  print("")
  print('    0   1   2   3   4')
  print('0   *   *   *   *   *')
  print('1   *   *   *   *   *')
  print('2   *   *   *   *   *')
  print('3   *   *   *   *   *')
  print('4   *   *   *   *   *')
  print("")

def processa(tab, linha, coluna):
  sair = 'n'
  while sair == 'n':
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
      print('Valores indisponíveis, tente novamente!')
    elif tab[linha][coluna] == 1:
      print("")
      for i in range(len(tab)):
        for m in range(len(tab[i])):
          if linha==i and coluna==m:
              print('0',end=' - ')
          else:
              print('*',end=' - ')
        print('\n')
      print('Vc clicou na bomba! BOOOOM!!!')
    else:
      print("")
      for i in range(len(tab)):
        for m in range(len(tab[i])):
          if linha==i and coluna==m:
              print('X',end=' - ')
          else:
              print('*',end=' - ')
        print('\n')
      print('Boa jogada!') 
    print("")
    sair = input('Deseja sair? (s/n) ')
    print("")
    if sair =='s':
     print('Obrigado por jogar!')

def principal():
  t = [
       [0, 0, 1, 1, 0],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0]
  ]
  lin = 0
  col = 0
  exibir = exibe()
  process = processa(t, lin, col)

principal()