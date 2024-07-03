import pygame
import random

pygame.init()
pygame.font.init()

lista = ["amar", "azul", "acordado", "amargura", "assistir", "apetecer", "ascender", "arrojado", 
    "aprender", "alcançar", "atribuir", "anarquia", "amistoso", "arretado", "ajudante", 
    "atraente", "apoteose", "atrofiar", "adiantar", "arrancar", "afrontar", "abestado", 
    "bizarro", "bem", "buscar", "basculho", "bastardo", "bivolt", "bom", "brado", "brasileiro", 
    "burro", "bruma", "base", "brega", "bravo", "bonito", "bojo", "barganha", "beldade", 
    "bondade", "bola", "bajulador", "belo", "brasil", "bolo", "burrice", "bobo", "bruços", 
    "bônus", "biodiversidade", "cultura", "confiança", "como", "conserto", "circunstância", 
    "caos", "consequência", "casual", "cinismo", "cético", "conveniência", "compaixão", 
    "consonância", "cordial", "compartilhar", "complexo", "céu", "clichê", "critério", 
    "coragem", "consoante", "carência", "canalha", "coerente", "custódia", "colapso", "casa", 
    "caridade", "conhecer", "complexidade", "conforme", "descobrir", "defasagem", "desalento", 
    "diplomata", "democrata", "divertido", "destituir", "dezesseis", "discordar", "distraído", 
    "devolução", "disfarçar", "devastado", "desonesto", "dilapidar", "desabafar", "denunciar", 
    "desbocado", "devaneios", "despedida", "desamparo", "descrença", "desgastar", "debandada", 
    "desanimar", "deliciosa", "decrescer", "dessagrar", "desatacar", "elo", "entusiasta", 
    "estima", "emissão", "extorquir", "esboço", "extinguir", "explicar", "errante", "exalar", 
    "executar", "exclusão", "elegibilidade", "erudito", "eficaz", "estúpido", "expedido", 
    "exótico", "estereótipo", "fragmentado", "fascinante", "flanco", "factual", "fragrância", 
    "fito", "férias", "fiel", "funcionalidade", "feminino", "fechar", "fascínio", "fatores", 
    "franqueza", "fofoca", "fugir", "fenda", "fustigado", "fascinar", "fraternal", "flor", 
    "fundamentar", "ficha", "geocentrismo", "geringonça", "gesticular", "gene", "germânico", 
    "gelo", "gerenciamento", "gelatina", "germinação", "geek", "geleira", "gerencial", "gel", 
    "gelificante", "geba", "gesticulação", "gelar", "germinal", "geomorfológico", "geminação", 
    "geotermômetro", "gertrudes", "geologicamente", "georreferenciar", "geniculado", "gerontológico", 
    "gemar", "genialmente", "geminípara", "gengibirra", "honorário", "hidrópico", "herético", 
    "hiato", "haja", "honorários", "honrar", "higiene", "heterodoxo", "hígido", "herança", 
    "homeostase", "higienizar", "horrível", "heteronomia", "humanização", "habitat", "homeopático", 
    "hospício", "hansa", "herdar", "hibridismo", "hotel", "honroso", "hereditariedade", "hilariante", 
    "honorável", "hostilizado", "homizio", "hiância", "imanente", "insípido", "indiferença", 
    "intrínseca", "interesse", "instância", "insano", "intersecção", "intempestivo", "instável", 
    "idiossincrático", "intolerância", "inútil", "inevitável", "impor", "imiscuir", 
    "imperativo", "intervir", "incrédulo", "indissociável", "imaginação", "imagem", "inescrupuloso", 
    "ilusão", "injúria", "insolência", "ilustre", "jazigo", "jactar", "jogo", "jovialidade", 
    "justa", "justificação", "justaposto", "jamanta", "judiação", "jesuíta", "jazida", "javé", 
    "jogador", "jerivá", "jangada", "janeiro", "jarro", "joana", "jabiraca", "jandaia", 
    "jogatina", "julho", "junípero", "jubilamento", "joule", "jurígeno", "jararaca", "jaca", 
    "jarretar", "juncar", "judas", "jardar", "jejuar", "jogado", "judicativo", "jongo", 
    "japão", "karaokê", "ketchup", "kit", "kitchenette", "kickboxing", "kung fu", "kart", 
    "kartódromo", "kimono", "lua", "lembrança", "literalmente", "lucidez", "lastro", "lástima", 
    "laico", "lânguido", "ladainha", "linguagem", "ludibriado", "lenda", "louvor", "litigar", 
    "leite", "legítimo", "ladrão", "lassidão", "limitação", "liberal", "lema", "libido", 
    "light", "loucura", "lindeiro", "latino", "lacustre", "lapela", "livre-arbítrio", "libertino", 
    "légua", "levantamento", "lábia", "linhagem", "litigância", "logia", "limpo", "lutar", 
    "lúbrico", "mesmo", "menção", "método", "martírio", "mostrar", "mercê", "melindre", 
    "maroto", "mediador", "moderado", "monogâmico", "memória", "miliciano", "manutenção", 
    "manter", "marrento", "moção", "misticismo", "morar", "metafísica", "mutável", "mameluco", 
    "modesta", "modo", "mentor", "manifesto", "medida", "mancomunado", "moralista", "metonímia", 
    "massivo", "murmúrio", "monastério",     "mau", "nascimento", "nativo", "natural", "navegante", "necessidade", "neto", "nível", "nobre", "nadadeira", "narguilé", "navalha", "nave", "navio", "nebulizador", "niple", "obcecado", "otimizar", "oneroso", "outro", "opressão", "obtuso", "orla", "oblação", "onerar", "obstruir", "obstrução", "opcional", "orvalho", "olá", "obra", "oásis", 
    "ordenado", "oferta", "online", "ocasionalmente", "oficial", "ocupado", "ordeiro", 
    "obrigada", "ourives", "osso", "oportunismo", "opróbio", "obediente", "off", "objetar", 
    "outdoor", "originário", "organizado", "oscular", "olfato", "operacional", "paciência", 
    "problema", "pejorativo", "preceito", "proposição", "paralelo", "primordial", "pragmatismo", 
    "pesar", "perseverar", "providência", "pela", "prazer", "postergar", "pudor", "pitoresco", 
    "patente", "prosélito", "parecer", "preponderante", "ponderado", "propiciar", "práxis", 
    "proeza", "puder", "pleito", "passiva", "preterido", "preservar", "prosperidade", "pulha", 
    "pátria", "proposta", "perfazer", "patológico", "quadro", "qualidade", "quase", "quatro", 
    "quebrado", "queda", "queijo", "queimar", "queixa", "quente", "querer", "quero", "questão", 
    "química", "quilate", "quilômetro", "quimera", "quindim", "quiosque", "quociente", "quota", 
    "quintal", "quinhão", "quarto", "quieto", "quiver", "quorum", "quente", "quinteto", "quartzo", 
    "quadrado", "quasar", "quebra", "quadro", "qualquer", "quartel", "queijo", "química", "química", 
    "quimono", "quilombo", "quintal", "querido", "querido", "quilograma", "quarentena", "quinhão", 
    "quadrúpede", "quarto", "rabisco", "rabo", "raça", "rachado", "radar", "rádio", "rádix", "raia", 
    "raio", "raiva", "raiz", "rajada", "ralar", "ralo", "ramal", "rã", "ranger", "ranho", "ranzinza", 
    "rapadura", "rapariga", "rapaz", "rapel", "rápido", "rapina", "raposa", "raquete", "rasante", 
    "rasgar", "raso", "rastro", "ratificar", "rato", "razoável", "razão", "realeza", "realidade", 
    "rebanho", "rebelde", "recado", "receber", "recessão", "recibo", "recipiente", "recitar", 
    "recobrar", "recolher", "recordar", "recurso", "redemoinho", "sábio", "sabão", "sabedoria", 
    "saber", "saborear", "sabor", "sacada", "saco", "sacrifício", "sádico", "sagacidade", "saga", 
    "sagrado", "saída", "salada", "salário", "saldo", "salgado", "saliva", "salmão", "salmo", 
    "salpicado", "salsa", "saltador", "saltar", "salto", "samba", "sâmbico", "sanatório", "sangue", 
    "santa", "santo", "sapa", "sapo", "saque", "saracoteio", "sarjeta", "sarna", "sarna", "sátira", 
    "satisfação", "sazonal", "saudável", "saudade", "saudar", "saúde", "saudoso", "seara", "sebo", 
    "seção", "tabaco", "tábua", "taco", "tática", "taberneiro", "tabuleiro", "tábula", "tacão", 
    "táctil", "tagarela", "tamanho", "tamanco", "tâmara", "tampo", "tampar", "tandem", "tanga", 
    "tango", "tanque", "tanto", "tarde", "tarefa", "tártaro", "tarugo", "tascar", "tatu", "tatuagem", 
    "tatuar", "teatro", "tecido", "tecla", "teclar", "tecnologia", "teimoso", "telhado", "telha", 
    "telescópio", "telúrico", "tempo", "tenda", "tênis", "tenor", "tentar", "tentação", "tênue", 
    "teor", "teórico", "ter", "terra", "terraço", "ubíquo", "uberaba", "ubá", "ubi", "ubíqua", "ubíquas", 
    "ubre", "úlcera", "ulisse", "ultimato", "último", "umidade", "único", "unidade", "uniforme", 
    "unificar", "unilateral", "unir", "universal", "universidade", "urbano", "urgente", "urna", 
    "urubu", "urze", "usufruir", "usual", "usura", "usurpador", "utilidade", "utilitário", "utilizar", 
    "utopia", "utrículo", "uva", "vadio", "validação", "vapor", "vasta", "veloz", "vênia", "veneno", 
    "verídico", "vermelho", "verão", "vestido", "vexatório", "viabilidade", "xadrez", "xale", "xangô", 
    "xará", "xarope", "xeque", "xícara", "xiita", "xilogravura", "xodó", "xoxo", "xote", "xuxa", 
    "xícara", "xaxim", "xênon", "xerife", "xerox", "xexéu", "xará", "xadrezista", "xamã", "xamânico", 
    "xanadu", "xará", "xará", "xávega", "xavante", "xeque-mate", "xenofobia", "xereca", "xerox", 
    "xicara", "xilogravura", "xilofone", "xiririca", "xixi", "xodó", "xucro", "xuxu", "zoada", "zombar", 
    "zoológico", "zoom", "zoonomia", "zoomorfismo", "zorra", "zulu", "zumbido", "zumbi", "zumbir", "zuílo", "zulu", "zumbi", "zunir", "zunzum", "zunzunzum", "zuízo", "zúrico", "zuzum", "zíper", "zózimo", "zuísmo", "zuíz", "zóxis", "zuízo", "zíper", "zoada", "zoa", "zoada", "zoada", "zoada", "zoada", "zoada", "zoada"]

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

gameloop = True
while gameloop:
    tela.fill(cor_fundo)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gameloop = False
        elif evento.type == pygame.KEYDOWN:
            letra = evento.unicode.upper()
            if letra.isalpha() and len(letra) == 1:
                if letra in sorte and letra not in letras_acertadas:
                    letras_acertadas.append(letra)
                elif letra not in sorte and letra not in letras_erradas:
                    letras_erradas.append(letra)
    
    mostrar_palavra(tela, sorte, letras_acertadas)
    mostrar_letras_erradas(tela, letras_erradas)
    desenhar_forca(tela, len(letras_erradas))

    if set(sorte) <= set(letras_acertadas):
        texto_vitoria = fonte_media.render("Você Venceu!", True, cor_texto)
        tela.blit(texto_vitoria, (500 - texto_vitoria.get_width() // 2, 300))
    elif len(letras_erradas) >= 6:
        texto_derrota = fonte_pequena.render(f"Você Perdeu! Era: {sorte}", True, cor_texto)
        tela.blit(texto_derrota, (500 - texto_derrota.get_width() // 2, 250))
   
    pygame.display.flip()

pygame.quit()
