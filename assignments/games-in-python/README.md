
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivos

Construir o clássico jogo da forca (Hangman) em Python para praticar manipulação de strings, laços, condicionais e entrada do usuário. O estudante irá implementar a lógica do jogo, tratar entradas inválidas e apresentar mensagens claras de vitória/derrota.

## 📝 Tarefas

### 🛠️	Implementar o jogo Hangman

#### Description
Escreva um script Python que execute o jogo da forca no terminal. O programa deve selecionar uma palavra aleatória de uma lista, permitir que o jogador chute letras, mostrar o progresso com underscores e espaços, e terminar quando a palavra for adivinhada ou as tentativas se esgotarem.

#### Requirements
Completed program should:

- Selecionar uma palavra aleatória a partir de uma lista embutida ou de um arquivo `words.txt`.
- Aceitar palpites do usuário (uma letra por vez) e ignorar entradas inválidas (não letras, mais de uma letra, ou letras já chutadas).
- Exibir o progresso da palavra usando underscores separados por espaços (ex.: `_ a _ _ _`).
- Mostrar a lista de letras já chutadas e o número de tentativas incorretas restantes.
- Diminuir as tentativas restantes apenas para palpites incorretos.
- Finalizar o jogo com uma mensagem de vitória (quando todas as letras forem reveladas) ou de derrota (quando as tentativas chegarem a zero) e revelar a palavra correta.

Exemplo de execução (fluxo simplificado):

```
Palavra: _ _ _ _ _
Adivinhe uma letra: a
Progresso: _ a _ _ _
Tentativas restantes: 5
```


### 🛠️	Extras (opcional)

#### Description
Adicione funcionalidades opcionais para estender o jogo e desafiar-se além dos requisitos mínimos.

#### Requirements
Completed program may include one or more of the following:

- Ler a lista de palavras a partir de um arquivo `words.txt` e tratar palavras vazias/comment lines.
- Implementar níveis de dificuldade (ex.: mais tentativas com palavras curtas, menos tentativas com palavras longas).
- Permitir reiniciar o jogo sem reiniciar o script.
- Exibir arte ASCII progressiva do boneco da forca conforme as tentativas são gastas.

