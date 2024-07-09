import pygame
import random

pygame.init()
pygame.font.init()

lista = ["abacate", "abacaxi", "abajur", "abelha", "abrigo", "acordeao", "acucar", "adaga",     "advinhacao", "afago", "afobamento", "agente", "agulha", "agua", "airbag", "alarme", "alberca", "album", "alface", "algema", "balanca", "banco", "banda", "barco", "barroco", "barriga", "basquete", "batata", "bateria", "bebe", "beijaflor", "belchior", "biblioteca", "bicicleta", "bigode", "bijuteria", "bilhete", "binoculo", "biografia", "biscoito", "cabana", "caderno", "cafe", "cagado", "caju", "calca", "camera", "camisa", "caminhao", "campainha", "caneta", "cao", "capela", "capim", "caramba", "caramelo", "carbonara", "cartaz", "casa", "casamento", "dado", "danca", "dedetizacao", "defesa", "degrau", "delirio", "dente", "deposito", "desejo", "desodorante", "destrave", "detector", "detonador", "diafragma", "dicionario", "dinheiro", "dinossauro", "diploma", "direcao", "discipulo",
"efeito", "eixo", "eletricista", "elefante", "elogio", "embaixada", "empada", "empreiteiro", "enigma", "enredo", "ensopado", "entrevista", "envelope", "espada", "especie", "espinhafre", "esporte", "esposa", "esqueleto", "estante", "faca", "faculdade", "fafa", "fogueira", "folha", "fome", "formiga", "forte", "foto", "framboesa", "frasco", "freio", "frio", "fruta", "fumaca", "funcao", "fundo", "furacao", "fuso", "futilidades","gabinete", "gaiola", "galinha", "garrafa", "gato", "geleia", "gelo", "genio", "girafa", "gol","golfinho", "goma", "gordo", "gorila", "grama", "gravata", "grego", "grito", "gruta", "guarana",
"habilidade", "hamburguer", "harpa", "helice", "heroi", "horta", "hospital", "hotel", "humor", "furacao",
"iate", "idade", "ideia", "idiota", "ioga", "iogurte", "ilha", "imaginacao", "impressora", "incendio",
"jaboticaba", "jacare", "jaleco", "jalada", "janela", "jantar", "jaqueta", "jardim", "jarro", "jazz",
"lapis", "laranja", "lebre", "legrao", "legiao", "legume", "lentilha", "leoa", "leque", "letra",
"liberdade", "libra", "livro", "lixo", "locador", "lobo", "local", "logica", "lote", "louca",
"maca", "macaco", "maquina", "madeira", "madrinha", "mae", "mago", "maia", "maique", "majestade",
"maldade", "mama", "mamao", "manga", "manha", "mapa", "mar", "maria", "marido", "martelo",
"nariz", "nascimento", "natureza", "navegador", "neblina", "necessidade", "negocio", "negociacao", "negro", "nenem", "nervoso", "nobre", "noite", "nome", "noticia", "nuvem", "numero", "nylon", "noiva", "objeto", "observador", "oceano", "oculos", "orelha", "orfanato", "orgulho", "origem", "ostra", "ovelha",
"paciencia", "padeiro", "padaria", "pagina", "paixao", "palco", "panelinha", "papai", "papel", "parafuso", "queijo", "quentel", "quimica", "quiosque", "quitar", "rabada", "rabo", "radar", "raio", "raposa", "rato", "refeicao", "regra", "relogio", "relampago", "sabor", "sabotador", "saco", "sacola", "sacolao", "sapo", "sapato", "sardinha", "saturado", "seguranca", "taberna", "tabela", "tapete", "tampa", "tatu", "taverna", "tecido", "teto", "tinta", "tipo", "urso", "urubu", "urgencia", "usina", "uva", "vaca", "vadio", "vagao", "vaidade", "validade", "valsa", "vampiro", "vapor", "varanda", "vaso",
"whisky", "windsurf", "xadrez", "xerife", "yoga", "zebra", "zinco", "abobora", "abobrinha", "acucareiro", "adega", "agenda", "aguia", "albumina", "alcatra", "alface", "algoritmo",
"alho", "alicate", "almofada", "aluno", "amendoim", "amor", "anel", "animal", "aniversario", "ano",
"antena", "anuncio", "apartamento", "aplauso", "arara", "arco", "arroz", "artista", "asa", "assalto",
"assistente", "astronauta", "atleta", "aventura", "aviao", "azulejo", "bailarina", "bala", "balanca", "baleia", "banheiro", "banquete", "banquinho", "barulho", "batalha", "bebida", "bebe", "bibliotecario", "bicicleta", "bife", "bola", "bolo", "bolsa", "bombom", "boneca", "borboleta", "botao", "brinquedo", "brocolis", "bruxa", "cabide", "cabine", "cabra", "cachecol", "cadarco", "cadeira", "cafezinho", "caixa", "cajado", "calca", "calendario", "camarao", "camelo", "caminho", "campainha", "campeao", "canario", "caneca", "canguru", "canivete",
"capacete", "capitao", "capote", "carimbo", "carne", "carro", "carteira", "cartola", "cartucho", "casaco", "castelo", "castor", "cauda", "caule", "caverna", "cebolinha", "cesta", "chaleira", "champanhe", "chave", "chiclete", "chocolate", "chuva", "ciclista", "cinto", "circo", "cogumelo", "colar", "cometa", "comida","computador", "concerto", "concha", "confete", "conquista", "conversa", "coracao", "coragem", "coroa", "corredor", "costela", "cotovelo", "cristal", "cubo", "cueca", "cultura", "cupcake", "curiosidade", "curva", "dado", "dedo", "defesa", "dentista", "desafio", "descoberta", "deserto", "detalhe", "deus", "dia", "diamante", "dica", "dicionario", "dificuldade", "dinamite", "dinheiro", "dinossauro", "direito", "disfarce", "diversao", "dobra",
"doce", "documento", "doenca", "dolar", "dormitorio", "dragao", "drama", "droga", "duvida", "edificio",
"edredom", "educacao", "efeito", "elevador", "elefante", "elemento", "elmo", "email", "emblema", "empregado","enchente", "encontro", "energia", "enfermeira", "engrenagem", "enigma", "enlatado", "enxame", "equilibrio", "escada","escaravelho", "escola", "escorregador", "escoteiro", "esfinge", "espelho", "esqueleto", "estacao", "estatua", "esteira","estomago", "estrela", "estudante", "evolucao", "exemplo", "experiencia", "explosao", "fabrica", "fada", "familia","fantasma", "farol", "fase", "faxineira", "felicidade", "feriado", "ferro", "festa", "fevereiro", "fibra","filme", "filtro", "fim", "fio", "foguete", "folclore", "fone", "fonte", "forno", "fosforo","franja", "frase", "freira", "fruta", "fuga", "fumante", "futebol", "futuro", "gaiola", "garagem","garfo", "gasolina", "gaveta", "gelo", "genero", "gigante", "girassol", "gloria", "goleiro", "gorro","gramatica", "grandeza", "granizo", "grao", "gravidade", "guarda-chuva", "guerreiro", "guitarra", "hamburguer", "harpa","heranca", "herbicida", "heroismo", "higiene", "historia", "hoje", "hora", "horario", "hortela", "hospital","hotel", "humano", "humorista", "igreja", "igualdade", "ilha", "imagem", "impacto", "impressao", "incenso","inicio", "inseto", "instante", "interesse", "inverno", "iodo", "janela", "jarro", "jaula", "jogador","jogo", "joia", "jornal", "jovem", "juba", "julho", "juliana", "junta", "justica", "ketchup","kit", "labirinto", "lacre", "laje", "lanche", "lanterna", "lapis", "lapiseira", "laranja", "lata","lavadora", "leao", "legado", "leilao", "lembranca", "lenco", "lente", "leopardo", "letra", "levante","liberdade", "linha", "lingua", "lirio", "lista", "livro", "lobo", "lona", "luz", "macaco","machado", "macieira", "madrugada", "maduro", "magia", "mala", "maleta", "mamao", "mamute", "manequim","manga", "manicure", "manobrista", "mantimento", "manual", "marca", "marido", "marisco", "marmota", "martelo","massa", "materia", "matricula", "mau", "mausoleu", "meia", "melodia", "melro", "memoria", "mentira","mensagem", "menu", "mergulho", "metal", "metro", "microfone", "milagre", "milho", "minuto", "missao","modelo", "molho", "montanha", "moqueca", "morcego", "morfina", "morte", "mosquito", "mostarda", "motivo","mundo", "muralha", "museu", "mutante", "nada", "nadar", "namoro", "nariz", "natal", "nave","necessidade", "negociante", "neve", "noite", "nota", "novela", "novidade", "numero", "nunca", "nutricao","obra", "obrigacao", "ocasioes", "oceano", "oferta", "oleo", "olhar", "ombro", "ondas", "opiniao","oracao", "orca", "ordem", "orelha", "origami", "orquidea", "ouro", "ovelha", "ovo", "pacote","paciencia", "palavra", "palco", "palha", "palito", "panda", "pano", "pao", "papagaio", "papel",
"parada", "parque", "partida", "passado", "passarinho", "passaro", "passo", "patente", "patinho", "patio","pato", "pavio", "pavimento", "paz", "peao", "pecado", "pechincha", "pedal", "pedra", "peixe",
"pele", "pendulo", "pente", "pequeno", "pera", "percevejo", "perfume", "pergunta", "perna", "peru",
"pesadelo", "pesca", "pesquisa", "pessoa", "petisco", "peste"]

contador = 0
def sortear_nome():
    return random.choice(lista).upper()

sorte = sortear_nome()
letras_acertadas = []
letras_erradas = []

cor_texto = (255, 255, 255)
cor_fundo = (75, 0, 130)

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Forca!")
fonte = pygame.font.Font(None, 58)
fonte_pequena = pygame.font.Font(None, 34)
fonte_media = pygame.font.Font(None, 52)

estado_jogo = "menu"
pontos = 0

def desenhar_forca(tela, erros):
    # Desenhando a estrutura da forca
    base_x, base_y = 20, 500
    pygame.draw.line(tela, cor_texto, (base_x, base_y), (base_x + 200, base_y), 6)
    pygame.draw.line(tela, cor_texto, (base_x + 100, base_y), (base_x + 100, base_y - 400), 10)
    pygame.draw.line(tela, cor_texto, (base_x + 100, base_y - 400), (base_x + 250, base_y - 400), 10)
    pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 400), (base_x + 250, base_y - 350), 10)

    if erros > 0:
        pygame.draw.circle(tela, cor_texto, (base_x + 250, base_y - 320), 30, 10) # Cabeça
    if erros > 1:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 290), (base_x + 250, base_y - 200), 10) # Tronco
    if erros > 2:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 250), (base_x + 200, base_y - 300), 10) # Braço esquerdo
    if erros > 3:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 250), (base_x + 300, base_y - 300), 10) # Braço direito
    if erros > 4:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 200), (base_x + 200, base_y - 150), 10) # Perna esquerda
    if erros > 5:
        pygame.draw.line(tela, cor_texto, (base_x + 250, base_y - 200), (base_x + 300, base_y - 150), 10) # Perna direita

def mostrar_palavra(tela, palavra, letras_acertadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_acertadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    texto = fonte.render(exibicao, True, cor_texto)
    tela.blit(texto, (500 - texto.get_width() // 2, 467))  # Abaixo da força

def mostrar_letras_erradas(tela, letras_erradas):
    texto = fonte_pequena.render("Erros: " + ", ".join(letras_erradas), True, cor_texto)
    tela.blit(texto, (10, 10))

def desenhar_botao(tela, texto, x, y, largura, altura):
    pygame.draw.rect(tela, (0, 0, 0), (x, y, largura, altura))
    pygame.draw.rect(tela, cor_texto, (x+2, y+2, largura-4, altura-4))
    texto_botao = fonte_pequena.render(texto, True, (0, 0, 0))
    tela.blit(texto_botao, (x + (largura - texto_botao.get_width()) // 2, y + (altura - texto_botao.get_height()) // 2))

def verificar_clique(x, y, largura, altura, pos):
    if x < pos[0] < x + largura and y < pos[1] < y + altura:
        return True
    return False

gameloop = True
while gameloop:
    tela.fill(cor_fundo)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gameloop = False
        elif evento.type == pygame.KEYDOWN and estado_jogo == "jogando":
            letra = evento.unicode.upper()
            if letra.isalpha() and len(letra) == 1:
                if letra in sorte and letra not in letras_acertadas:
                    letras_acertadas.append(letra)
                elif letra not in sorte and letra not in letras_erradas:
                    letras_erradas.append(letra)
        elif evento.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "menu":
            if verificar_clique(300, 250, 200, 60, evento.pos):
                estado_jogo = "jogando"
                sorte = sortear_nome()
                letras_acertadas = []
                letras_erradas = []
        elif evento.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "vitoria":
            if verificar_clique(300, 350, 200, 60, evento.pos):
                estado_jogo = "jogando"
                sorte = sortear_nome()
                letras_acertadas = []
                letras_erradas = []
                pontos += 1
        elif evento.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "derrota":
            if verificar_clique(300, 350, 200, 60, evento.pos):
                estado_jogo = "jogando"
                sorte = sortear_nome()
                letras_acertadas = []
                letras_erradas = []
                pontos = 0

    if estado_jogo == "menu":
        desenhar_botao(tela, "Play", 300, 250, 200, 60)
    elif estado_jogo == "jogando":
        mostrar_palavra(tela, sorte, letras_acertadas)
        mostrar_letras_erradas(tela, letras_erradas)
        desenhar_forca(tela, len(letras_erradas))
        texto_pontos = fonte_pequena.render(f"Pontos: {pontos}", True, cor_texto)
        tela.blit(texto_pontos, (650, 10))
        
        if set(sorte) <= set(letras_acertadas):
            estado_jogo = "vitoria"
        elif len(letras_erradas) >= 6:
            estado_jogo = "derrota"
    elif estado_jogo == "vitoria":
        texto_vitoria = fonte_media.render("Você Venceu!", True, cor_texto)
        tela.blit(texto_vitoria, (400 - texto_vitoria.get_width() // 2, 250))
        desenhar_botao(tela, "Continuar", 300, 350, 200, 60)
    elif estado_jogo == "derrota":
        texto_derrota = fonte_pequena.render(f"Você Perdeu! Era: {sorte}", True, cor_texto)
        tela.blit(texto_derrota, (400 - texto_derrota.get_width() // 2, 250))
        desenhar_botao(tela, "Tente Novamente", 300, 350, 200, 60)
    
    pygame.display.flip()

pygame.quit()
