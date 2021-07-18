#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some jokes copied fro
https://gist.githubusercontent.com/henrycunh/75abcf44146d5d9c0714932a386dbbf1/raw/558b97a002d578998720d76458641d4782c97d34/trocadilhos.json

"""
import random
import json
import os
from aiohttp import web

# Partially extracted from
PIADAS = [
    {
        "question": "Qual é a profissão do Homem Aranha?",
        "answer": "Desenvolvedor Web",
    },
    {"question": "Qual é o estado dos EUA que te eletrifica?", "answer": "Ohio."},
    {
        "question": "Por que o monge foi ao hospital?",
        "answer": "Porque ele é paciente.",
    },
    {"question": "Qual o time mais quente de todos?", "answer": "Bota-fogo."},
    {
        "question": "Por que o cachorro ia pra escola todos os dias?",
        "answer": "Porque ele tinha auaula.",
    },
    {"question": "Qual o produto tensoativo que sabe de tudo?", "answer": "Sabão."},
    {
        "question": "Quem é o rei dos produtos de espantar insetos?",
        "answer": "É o Rei-pelente.",
    },
    {
        "question": "Por que o magrelo tem que tomar banho com os braços abertos?",
        "answer": "Para não ser engolido pelo ralo.",
    },
    {
        "question": "Qual o ator que livra as pessoas das dores?",
        "answer": "Malvino Salva-dor.",
    },
    {
        "question": "Por que as vogais A, E, I e O foram rejeitadas pela banda Scorpions?",
        "answer": "Porque eles Still Love U.",
    },
    {"question": "Qual a carne que é cheia de panos?", "answer": "Frango Empanado."},
    {
        "question": "Por que o Papai Noel não tem assadura?",
        "answer": "Porque seu saco já é vermelho.",
    },
    {"question": "Qual é a bebida que corre?", "answer": "Rum."},
    {
        "question": "Você está em uma estrada e vê vários postos um perto do outro. Por que isso acontece?",
        "answer": "Porque os-postos se atraem.",
    },
    {"question": "Qual animal não gosta do amanhã?", "answer": "Rinocer-ontem."},
    {
        "question": "O que acontece se um panda tiver vários filhotes?",
        "answer": "Vira uma pandemia.",
    },
    {"question": "Qual a fruta predileta da cigana?", "answer": "O Li Mão."},
    {
        "question": "Qual é o tipo de música favorito dos mortos?",
        "answer": "R.I.P-Hop.",
    },
    {"question": "O que é que tem no meio do ovo?", "answer": "A gema."},
    {
        "question": "Por que a loira entrou com muitos espelhos na faculdade de engenharia?",
        "answer": "Porque ela é engenheira se-viu.",
    },
    {
        "question": "Qual é a cantora que não se adapta ao meio urbano?",
        "answer": "Vanessa da Mata.",
    },
    {
        "question": "Qual é o super-herói que toma chá e depois dá um salto pequeno?",
        "answer": "Chá-pulinho.",
    },
    {"question": "Qual é a ave que está sempre enrijecida?", "answer": "An-durinha."},
    {
        "question": "Qual é a ave que serve de automóvel para um parasita aracnídeo?",
        "answer": "Carro-a-pato.",
    },
    {
        "question": "Porque o principal narrador esportivo da Globo adora narrar jogos da Argentina?",
        "answer": "Porque é Galvão Buenos-Aires.",
    },
    {
        "question": "Que tipo de negócio abriram os ursos da China?",
        "answer": "Uma pandaria.",
    },
    {"question": "Qual o filósofo favorito do cavalo?", "answer": "Trotsky."},
    {
        "question": "Qual é a ferramenta que sempre aponta onde as pessoas e coisas estão?",
        "answer": "Ali-cate.",
    },
    {
        "question": "O que o leitão foi fazer na loja de parafusos?",
        "answer": "Foi procurar a porca.",
    },
    {
        "question": "O que o boi respondeu para a vaca, quando ela o perguntou se ele gostava bastante dela?",
        "answer": "Muuuuuuuuuuuuito!",
    },
    {"question": "Como se chama o campeonato de anedotas?", "answer": "Olim-piadas."},
    {
        "question": "Qual a reação de um mecânico depois de contarem uma piada sem graça para ele?",
        "answer": "Dizer que não achou graxa nenhuma.",
    },
    {
        "question": "Qual o tipo de violência que o super-herói do martelo não admite?",
        "answer": "A Thortura.",
    },
    {"question": "Qual a doença do sacristão?", "answer": "Sinus-ite."},
    {
        "question": "Por que temos vacas e bois próximos ao nosso estômago?",
        "answer": "Porque temos o intestino deu-gado.",
    },
    {
        "question": "Qual o tipo de pessoa o Papai Noel gosta?",
        "answer": "De puxa-saco.",
    },
    {
        "question": "Qual é o ramo da medicina que faz uma ligação para a irmã de sua mãe?",
        "answer": "Alopatia.",
    },
    {
        "question": "O que acontece se um panda tiver vários filhos?",
        "answer": "Ele vira um pandeiro.",
    },
    {"question": "Quando é que o Renato Aragão acorda?", "answer": "Didi-a."},
    {
        "question": "O que é que, quando o pai nasce a filha já esta andando?",
        "answer": "Fumaça.",
    },
    {
        "question": "Qual é o time mais odiado pelo os bombeiros?",
        "answer": "Botafogo",
    },
    {
        "question": "O que você deve fazer quando estiver triste?",
        "answer": "Abraçar o sapato, porque o sapato com-sola.",
    },
    {
        "question": "Qual o carro em que o Cebolinha manda as pessoas pararem?",
        "answer": "Ô-Pala.",
    },
    {
        "question": "Você sabe qual é a comida preferida do topógrafo?",
        "answer": "Frângulo.",
    },
    {"question": "Como se fala bombeiro em japonês?", "answer": "Takágua Naxama."},
    {
        "question": "Qual a rede social que os mineiros mais usam?",
        "answer": "Uaitsapp.",
    },
    {"question": "Qual é a massa do caderno?", "answer": "A massa folhada."},
    {
        "question": "Três mulheres estavam com picolés nas mãos. Uma estava chupando o picolé, outra estava mordendo o picolé e outra estava lambendo o picolé. Qual delas era a casada?",
        "answer": "A que estava com anel no dedo.",
    },
    {
        "question": "Qual o banco em que uma letra se transforma em outra letra?",
        "answer": "É o I-tá-U.",
    },
    {"question": "Qual a fruta que é parente da porta?", "answer": "É a Maçã-Neta."},
    {"question": "Qual é a peça de roupa preferido do Thor?", "answer": "PaleThor."},
    {
        "question": "Qual a cantora que é o primeiro alce do mundo?",
        "answer": "Alce-One.",
    },
    {
        "question": "Um bêbado estava na rua quando chegou um carro e buzinou. O que o bêbado respondeu?",
        "answer": "Eu também bibi.",
    },
    {
        "question": "Qual a diferença entre a cachaça e a mulher?",
        "answer": "A cachaça dá dor de cabeça só um dia.",
    },
    {
        "question": "Por que o português jogou o arroz inteiro do pacote dentro do pote de açúcar?",
        "answer": "Para comer arroz doce.",
    },
    {
        "question": "Por que os lustres não prestam atenção para escuridão?",
        "answer": "Porque eles tem focos luminosos.",
    },
    {
        "question": "O que é um cachorro afinado, que entende de música?",
        "answer": "É um cãotor.",
    },
    {
        "question": "O que é um objeto cortante em poder de um cachorro?",
        "answer": "Um cão-nivete.",
    },
    {
        "question": "Por que o maior dramaturgo de língua inglesa é considerado um cavalheiro quando tenta ir ao banheiro, mas está ocupado?",
        "answer": "Porque quando ele bate e respondem que tem gente, ele diz em seguida: Shake-espera.",
    },
    {
        "question": "Por que na cidade de Palmas as mulheres nunca conseguem molhar o cabelo?",
        "answer": "Porque lá elas usam Touca-ntins.",
    },
    {
        "question": "Por que a loira pediu um envelope redondo no escritório onde trabalha?",
        "answer": "Porque seu chefe a pediu para entregar uma circular.",
    },
    {"question": "Qual o veículo que é mulher do lanche?", "answer": "Lancha."},
    {
        "question": "O tio de Pedro tem 4 filhas, Lala, Lele, Lili, Lolo. Qual falta?",
        "answer": "Nenhuma, porque já tem 4.",
    },
    {
        "question": "Qual o molho de tomate preferido dos gatos?",
        "answer": "É o Cat-chup.",
    },
    {
        "question": "Qual o eletrodoméstico do vulcão?",
        "answer": "É a máquina de lava.",
    },
    {
        "question": "Um homem levou um pedaço de queijo pro hospício e um dos pacientes subiu em cima do queijo. Qual o nome da série?",
        "answer": "Um Maluco no Pedaço.",
    },
    {
        "question": "O que pensaram os outros convidados quando viram o Zangado chegar na festa sem a Branca de Neve?",
        "answer": "Ah, Não!",
    },
    {
        "question": "Qual o campeonato que tira as suas dores?",
        "answer": "Liberta-dores",
    },
    {"question": "Qual é a vestimenta preferida do Batman?", "answer": "Bat-ina."},
    {
        "question": "Por que um atleta dormiu na balança de uma farmácia?",
        "answer": "Para que quando acordasse fizesse um levantamento de peso.",
    },
    {"question": "Qual o peixe que é parceiro de todo mundo?", "answer": "Truta."},
    {
        "question": "Por que as roupas amassadas se estenderam sobre o trilho?",
        "answer": "Porque lá passa o Trem de Ferro.",
    },
    {
        "question": "Qual o médico que as pessoas atiram compostos orgânicos?",
        "answer": "Geraldo Álcool-Em-Mim.",
    },
    {"question": "Como se diz veterinário em japonês?", "answer": "Kuragato Nakasa."},
    {
        "question": "Qual é o alimento preferida do Thor no natal?",
        "answer": "Pane-Thor-ne.",
    },
    {
        "question": "Qual é o aparelho digital preferido do Thor?",
        "answer": "LapTHORp.",
    },
    {
        "question": "Por que a loira leva sabonete e shampoo pro pé de manga?",
        "answer": "Porque ela gosta de tomar banho de mangueira.",
    },
    {
        "question": "Qual a explosão que o Renato Aragão mais tem medo?",
        "answer": "É a Didi-namite.",
    },
    {
        "question": "O que a Oceania e a novela tem em comum?",
        "answer": "Que a Oceania é O Outro Lado do Mundo e a novela é O Outro Lado do Paraíso.",
    },
    {
        "question": "O menino estava assistindo desenho, e seu pai sem querer resvala na tomada e acaba desligando a TV. Qual o nome do desenho?",
        "answer": "Pô-pai.",
    },
    {
        "question": "Qual é a fruta que termina primeiro do que todas as outras?",
        "answer": "Jabuti-acaba.",
    },
    {"question": "Qual é o urso que nunca envelhece?", "answer": "Peter-Panda."},
    {
        "question": "Porque o urso começou a se coçar de repente?",
        "answer": "Porque ele era um urso empolar.",
    },
    {
        "question": "Um americano perguntou para o bom velhinho do natal: Papai, o senhor está bem?",
        "answer": "No well, respondeu o senhor...",
    },
    {
        "question": "O que disse uma pessoa após ter descoberto que havia comprado um óculos sem as lentes?",
        "answer": "Cuidado, é armação...",
    },
    {
        "question": "Por que as senhoras que vão à piscina gostam tanto de Helmmans?",
        "answer": "Porque elas só ficam de maiô-nesse.",
    },
    {
        "question": "Porque todos os tipos de carne não toleram os bifes macios?",
        "answer": "Porque elas são contra-filé.",
    },
    {
        "question": "Qual o estado brasileiro que anda de trem?",
        "answer": "Piauiiiiiiiiiiiiiiii.",
    },
    {
        "question": "Como a família portuguesa que mora no Brasil parou de gastar com oftalmologista?",
        "answer": "Mudando-se para Boa-Vista.",
    },
    {
        "question": "Qual é a capital brasileira que ensina a irmã a latir?",
        "answer": "Mana, au-aus.",
    },
    {
        "question": "Qual a cidade mais amarela do mundo?",
        "answer": "Yellows Angeles.",
    },
    {
        "question": "Qual é o cantor que poderia ser ortopedista?",
        "answer": "Caetano Vê-o-osso.",
    },
    {"question": "Qual o carro mais azedo que existe?", "answer": "Limão-zine."},
    {
        "question": "Por que um jardineiro estava cavando o chão da vila do Chaves?",
        "answer": "Porque ele queria achar o tesouro.",
    },
    {
        "question": "Qual o problema de saúde que nenhum anão terá?",
        "answer": "Pressão alta.",
    },
    {
        "question": "Qual é a fruta favorita dos maquinistas?",
        "answer": "Kiwiiiiiiiiiiiiiii!!!",
    },
    {
        "question": "Qual é a fruta que ameniza o calor de Ana?",
        "answer": "Abana-Ana.",
    },
    {
        "question": "Por que o estádo do Grêmio tem muitas abelhas?",
        "answer": "Porque Pedro Gerou-o-mel.",
    },
    {
        "question": "Dois textos eram incompletos e estavam participando de alguns campeonatos de futebol, o que um disse pro outro?",
        "answer": "Precisamos de título.",
    },
    {
        "question": "Qual o apresentador que tem olfato de animal?",
        "answer": "Rodrigo Faro.",
    },
    {"question": "Qual é o carro do exército?", "answer": "Kadett."},
    {
        "question": "Qual é a crença ou religião que está sempre conectada à internet?",
        "answer": "A Umbanda Larga.",
    },
    {
        "question": "Qual é o lugar da igreja que o Batman mais gosta?",
        "answer": "Bat-istério.",
    },
    {"question": "Qual é o animal preferido do Thor?", "answer": "OrniThorrinco."},
    {
        "question": "Meu fim me leva ao começo ou o inexiste, sou um caminho sem fim, oque eu sou?",
        "answer": "Um paradoxo.",
    },
    {
        "question": "Estou à sua volta, moro em seu coração, mas não posso ser compartilhado. O que eu sou?",
        "answer": "A solidão. Qualquer outro sentimento e até mesmo a sabedoria e conhecimento pode ser compartilhado.",
    },
    {
        "question": "Por que a loira comeu o telhado da casa?",
        "answer": "Porque ela era comi-lona.",
    },
    {
        "question": "Por que o anão não escuta o outro?",
        "answer": "Porque ele fala baixinho.",
    },
    {
        "question": "Qual o time de futebol em que um chinês observa um jogo de sinuca?",
        "answer": "Lee-ver-pool.",
    },
    {
        "question": "Qual o animal preferido do Renato Aragão?",
        "answer": "Didi-nossauro.",
    },
    {"question": "Qual time de futebol larga na frente?", "answer": "Na-Pole."},
    {
        "question": "Qual a atriz que faz cópias de imagens?",
        "answer": "Gisele Print.",
    },
    {
        "question": "Qual o lugar onde as pessoas mais fazem churros?",
        "answer": "Na enxurrada.",
    },
    {"question": "Qual é a função do Thor?", "answer": "CorreThor."},
    {"question": "Qual país que se você pisar, será preso?", "answer": "Cana-dá."},
    {
        "question": "Um jogador de futebol apareceu e virou líder de um time de um programa de domingo da Globo. Qual o nome do filme?",
        "answer": "Capitão Fantástico.",
    },
    {"question": "O que o goleiro utiliza para dormir?", "answer": "Trave-sseiro."},
    {
        "question": "Qual o aparelho luminário preferido do Thor?",
        "answer": "RefleThor.",
    },
    {"question": "Qual o animal mais fuxiqueiro que existe?", "answer": "A fo-foca."},
    {
        "question": "Qual é o animal peçonhento que trabalha com montaria?",
        "answer": "É o escor-peão.",
    },
    {
        "question": "Por que um determinado inseto voador não reclama de aterrissar nos piores locais possíveis?",
        "answer": "Por que Mari-pousa em qualquer lugar.",
    },
    {
        "question": "Qual é o nome da norma jurídica para pessoas com dificuldades de dicção por repetirem demais as sílabas das palavras?",
        "answer": "Lei de Gaga.",
    },
    {
        "question": "Tinham dez pessoas em cima de uma árvore jogando pastilhas garoto nas pessoas que passavam em baixo. Qual o nome do filme?",
        "answer": "Os Dez Manda Menta.",
    },
    {"question": "Qual o ovo mais escuro que existe?", "answer": "Ovinho tinto."},
    {
        "question": "Por que nunca falta energia no fundo do rio?",
        "answer": "Porque ele tem enguia elétrica.",
    },
    {
        "question": "Qual artista você não pode convidar para sua casa?",
        "answer": "O Eric... Claptomaniaco!",
    },
    {
        "question": "Do que as velhinhas mas sentem saudades?",
        "answer": "Da Ditadura!",
    },
    {
        "question": "Qual a semelhança entre o Uruguai e o YouTube?",
        "answer": "Que os dois tem um Monte-Vídeo.",
    },
    {
        "question": "No trânsito, como fazer para as dores corporais passarem mais depressa?",
        "answer": "É só pisar no acelera-dor.",
    },
    {
        "question": "Por que o envelope é tão medroso jogando baralho?",
        "answer": "Porque ele só guarda as cartas.",
    },
    {
        "question": "Por que as roupas devem se pendurarem nos cabides?",
        "answer": "Porque eles não tem mãos pra segurarem elas.",
    },
    {
        "question": "Qual a vodka que da tiros para os dois lados?",
        "answer": "Bala-lá-e-cá.",
    },
    {
        "question": "Qual o chocolate que espanta que espanta a capital do Equador?",
        "answer": "Xô-Quito.",
    },
    {"question": "Como se chama mil políticos presos?", "answer": "Um bom começo."},
    {"question": "O que desce chorando da escada?", "answer": "Balde."},
    {
        "question": "Por que o carro jamais é eletrocutado?",
        "answer": "Porque ele tem o para-choque.",
    },
    {
        "question": "Qual é a versão de Dragon Ball que o Vasco, Fluminense e Botafogo mais gostam?",
        "answer": "Kai.",
    },
    {"question": "Qual é o mosquito que a vaca tem medo?", "answer": "Muuuuriçoca."},
    {
        "question": "Por que um tigre auxiliava o idoso a andar?",
        "answer": "Porque ele era um tigre de bengala.",
    },
    {
        "question": "Quem é que, no Natal, anda com o saco cheio às costas subindo e descendo a rua?",
        "answer": "O carteiro, ou você acredita em Papai Noel?",
    },
    {
        "question": "Como um escritor termina um caso de amor?",
        "answer": "Com um ponto final.",
    },
    {
        "question": "Por que é que 'na casa do ferreiro tem espeto de pau'?",
        "answer": "Porque 'santo de casa não faz milagre'.",
    },
    {
        "question": "Entre médicos, qual deveria ser considerado engenheiro?",
        "answer": "Os que faz pontes de safena.",
    },
    {
        "question": "Quem é que bate na porta sem estar chamando ninguém?",
        "answer": "O marceneiro.",
    },
    {
        "question": "Que fazem os grandes costureiros, quando não têm o que fazer?",
        "answer": "Inventam moda.",
    },
    {
        "question": "Que pista levou o policial à certeza de que aquele carro, parado no estacionamento, era roubado?",
        "answer": "O motor estava quente, mas a placa fria.",
    },
    {"question": "Qual a profissão que aborrece?", "answer": "A de amolador."},
    {"question": "Como se chama o jornal do oculista?", "answer": "O globo ocular."},
    {
        "question": "Qual a carta que melhora a vida do carteiro?",
        "answer": "A carta de recomendação.",
    },
    {
        "question": "Qual o produto alimentício preferido dos escritores?",
        "answer": "A sopa de letrinhas.",
    },
    {
        "question": "Que escritor escreve um livro em menos de um minuto?",
        "answer": "Qualquer um: 'um livro'.",
    },
    {
        "question": "Qual o lugar onde o pescador pode até escolher o peixe?",
        "answer": "Na peixaria.",
    },
    {
        "question": "Por que um astrônomo sempre se frusta quando tenta estudar os grandes grupos de estrelas do Universo?",
        "answer": "Porque no telescópio, a visão é sempre nebulosa.",
    },
    {
        "question": "Quem é que se encarrega pessoalmente de transmitir os nossos desabafos, as nossas alegrias, exigências e consulta sem jamais ter contato conosco?",
        "answer": "O carteiro.",
    },
    {"question": "Qual é a capital preferida do Thor?", "answer": "PreTHORia."},
    {
        "question": "Qual a prótese que vive durante um longo período?",
        "answer": "É a denta-dura.",
    },
    {
        "question": "Qual a haste de metal que é uma operadora de TV?",
        "answer": "É o Alfi-NET.",
    },
    {"question": "Onde o Renato Aragão nasceu?", "answer": "Na Didi-namarca."},
    {"question": "Qual o país que sai pegando tudo?", "answer": "Catar."},
    {
        "question": "Por que a música foi na papelaria?",
        "answer": "Porque ela queria um clipe.",
    },
    {
        "question": "No salão de beleza, por que o português colocou uma grade sobre a cabeça?",
        "answer": "Porque ele queria um de-gradê.",
    },
    {"question": "Qual o jogador que trata água?", "answer": "Aguero."},
    {"question": "Qual é o jogador que não toma tiro?", "answer": "Dybala."},
    {"question": "Qual país do caribe é uma explosão?", "answer": "Granada."},
    {
        "question": "Nas obras, como fazer para a parede de tijolo ser recarregada?",
        "answer": "É só fazer um abaste-cimento.",
    },
    {
        "question": "Qual o ator que os operários sobem em cima dele?",
        "answer": "Vã-Andaime.",
    },
    {
        "question": "O que acontece se o coqueiro beber demais?",
        "answer": "Ele chapa o coco.",
    },
    {
        "question": "Estou acima das pessoas mais posso ficar a baixo delas, sou sólido e essencial para um lar quem eu sou?",
        "answer": "Terraço.",
    },
    {
        "question": "O que um jogador de futebol falou pro outro na hora de dar um pré-datado?",
        "answer": "Eu não tenho dinheiro, mas o Peter Cheque.",
    },
    {
        "question": "O que a ponte pequena disse para outra que cresceu?",
        "answer": "E agora, eu te vi-adulto.",
    },
    {
        "question": "Por que o fio sentiu frio?",
        "answer": "Porque ele estava desencapado.",
    },
    {"question": "Qual é a cerveja favorita dos cachorros?", "answer": "Glaciau-au."},
    {
        "question": "Qual é o animal mais preguiçoso que existe?",
        "answer": "A dor-minhoca.",
    },
    {
        "question": "Qual é o movimento que as próprias pessoas que curtem muito realizam?",
        "answer": "Fã-farra.",
    },
    {
        "question": "Por que o energético mais conhecido do mundo agora faz propaganda de marca de informática?",
        "answer": "Porque Red Bull te dá Asus!",
    },
    {
        "question": "Qual é o pão que o Ursinho Pooh mais gosta?",
        "answer": "Pão de Mel.",
    },
    {"question": "Qual é o brinquedo preferido do Thor?", "answer": "AuTHORama."},
    {
        "question": "Qual o conselho que o seu pai te dava para classificar as mulheres por tipo?",
        "answer": "Cate-gurias.",
    },
    {
        "question": "Qual é a fruta que é também é dois animais?",
        "answer": "Jabuti-Cabra.",
    },
    {
        "question": "Represento o amor, mas amor não posso ter, me desenham com 2 indicadores, mas como um punho da sua mão eu posso ser, que sou eu?",
        "answer": "O coração.",
    },
    {
        "question": "O que o pobre tem que se o rico comer ele morre?",
        "answer": "Nada. O pobre tem nada, e se o rico comer nada ele morre de fome.",
    },
    {"question": "Qual atriz é um peixe cartilaginoso?", "answer": "Claudia Arraia."},
    {"question": "Qual a planta dos sentimentos imediatos?", "answer": "Jacinto."},
    {
        "question": "O que é que diz um ratão de 100 quilos?",
        "answer": "Vem, vem gatinho.",
    },
    {"question": "O que é que se pede com o dedo?", "answer": "Ligação telefônica."},
    {
        "question": "O que é que perdido uma vez nunca mais se acha?",
        "answer": "O tempo.",
    },
    {
        "question": "Para que homem todos os outros tiram o chapéu?",
        "answer": "Para o barbeiro.",
    },
    {
        "question": "Qual a palavra que você usa quando se esquece das outras?",
        "answer": "Sinônimos.",
    },
    {"question": "O que nasce grande e morre pequeno?", "answer": "O sabão."},
    {
        "question": "O que é o que é entra na igreja de cabeça para baixo?",
        "answer": "O prego do sapato.",
    },
    {
        "question": "Qual o jogador de basquete que trabalha como faxineiro?",
        "answer": "Anderson Varre Chão.",
    },
    {"question": "Qual banda de rock que beija todo mundo?", "answer": "Kiss."},
    {
        "question": "Qual o cantor que se compara com as leis marítimas?",
        "answer": "Bob Mar-Lei.",
    },
    {"question": "Qual o aplicativo preferido do Thor?", "answer": "Play sThor."},
    {"question": "Qual a flor que diz estar se sentindo?", "answer": "Jacinto."},
    {"question": "Qual ator é símbolo de países?", "answer": "Antônio Bandeiras."},
    {
        "question": "Qual o planeta mais admirado do supermercado?",
        "answer": "Uau-Marte.",
    },
    {"question": "Qual a batata que todos devem respeitar?", "answer": "Lays."},
    {
        "question": "Qual o hipermercado preferido do número 4?",
        "answer": "Carre-Four.",
    },
    {
        "question": "Qual a universidade particular que quase tira um dez?",
        "answer": "Uni-nove.",
    },
    {
        "question": "Qual a diferença entre um limão e o Mr. Bean?",
        "answer": "Que o limão só faz careta quando é chupado.",
    },
    {
        "question": "Qual a cerveja que os de menores não podem beber?",
        "answer": "Proibida.",
    },
    {
        "question": "Qual o salgadinho que mais vai no jogo de futebol?",
        "answer": "A Torcida.",
    },
    {
        "question": "O que um bolo com frio disse pro outro?",
        "answer": "Precisamos de cobertura.",
    },
    {
        "question": "Por que o armário estava lotado?",
        "answer": "Porque todos queriam ver o jogo de panelas.",
    },
    {
        "question": "Por que Bob Marley é folgado?",
        "answer": "Porque ele quer que o arrasta-fari.",
    },
    {
        "question": "Tenho 5 maçãs, roubo de Joãozinho 5, quantas tartarugas tem no pote de doce?",
        "answer": "Duas, pois vassoura não assiste TV a noite.",
    },
    {
        "question": "Qual animal mais gosta de cantar em grupo?",
        "answer": "A cobra-coral.",
    },
    {
        "question": "Por que os padres amam açúcar?",
        "answer": "Porque eles abraçam um sacer-doce-o.",
    },
    {"question": "Qual é a comida favorito da piranha?", "answer": "Pirão."},
    {
        "question": "O que uma ave perguntou pra outra sobre o futebol?",
        "answer": "Meu time é o Flamingo, e o seu?",
    },
    {
        "question": "Por que um dos maiores apresentadores da Rede Globo não queria uma fazenda?",
        "answer": "Porque ele queria apenas uma Chacrinha.",
    },
    {
        "question": "Qual a doença que mais incomoda os gaúchos?",
        "answer": "Artri-tchê.",
    },
    {
        "question": "Por que Angelina não é considerada uma atriz completa?",
        "answer": "Porque para isso, Angelina além de Jô-Li, deveria ser Jô-Escrevi também.",
    },
    {
        "question": "Por que o ex-marido de Angelina Jolie é considerado um cara muito chato?",
        "answer": "Porque vive o Brad dando Pití.",
    },
    {
        "question": "Qual é o veículo de comunicação que sempre obverva você?",
        "answer": "É a Rede Te Vê.",
    },
    {
        "question": "Por que nos montes mais altos e frios da Suíça tem cachorros?",
        "answer": "Porque lá estão os au-aupes.",
    },
    {
        "question": "Qual é o legume favorito do menino de madeira que cresce o nariz?",
        "answer": "O Pepinóquio.",
    },
    {
        "question": "Qual a fruta que tem título de nobreza?",
        "answer": "Fruta-do-Conde.",
    },
    {
        "question": "Por que o português colocou a cama no guarda-roupas?",
        "answer": "Por que o médico o pediu para guardar leito.",
    },
    {
        "question": "O que o mineirinho pediu ao saber que no cardápio de um determinado restaurante só servia frutos do mar?",
        "answer": "Uma banana d'água.",
    },
    {
        "question": "Qual é o país onde as pessoas mais praticam musculação?",
        "answer": "Só-malha.",
    },
    {
        "question": "Qual é o animal que mais sente quando a temperatura está alta?",
        "answer": "A Calor-psita.",
    },
    {
        "question": "Qual animal é o melhor dos dançarinos?",
        "answer": "O tatu-re-bola.",
    },
    {
        "question": "Qual o celular que deixa você fazer o que quiser com ele?",
        "answer": "Ai pode.",
    },
    {
        "question": "Por que a roupa saiu correndo e pulou na banheira d'água?",
        "answer": "Porque ela só levava ferro.",
    },
    {
        "question": "Por que um homem vivia cheio de velas em sua casa?",
        "answer": "Porque ele era fã do Caetano Veloso.",
    },
    {
        "question": "Por que a galinha gorda estava batendo a cabeça no bebedouro elétrico?",
        "answer": "Porque ela queria um galão.",
    },
    {"question": "Qual é a profissão agente do Thor?", "answer": "CorreThor."},
    {"question": "O que o Thor mais gosta do banheiro?", "answer": "Thor-alha."},
    {"question": "Qual é a função de autoridade do Thor?", "answer": "PromoThor."},
    {
        "question": "Qual o jogador que larga as coisas de qualquer jeito?",
        "answer": "Se-dane.",
    },
    {
        "question": "Por que a vaca foi pra Alemanha?",
        "answer": "Porque ela queria ver Muuuuu-nique.",
    },
    {
        "question": "Por que a loira joga o relógio pela janela?",
        "answer": "Porque a hora voa.",
    },
    {
        "question": "Por que o Médico tem a letra feia?",
        "answer": "Porque ele não sabe escrever, só prescrever.",
    },
    {"question": "O que o gato faz quando está na rua?", "answer": "Engatinha."},
    {
        "question": "Por que os cães da Austrália ficam roucos?",
        "answer": "Porque a capital do país se chama cão-berra.",
    },
    {
        "question": "Por que os papéis e as folhas tem medo do Rio de Janeiro?",
        "answer": "Porque eles fazem picadinho.",
    },
    {
        "question": "Qual a ave que quer matar as vacas imediatamente em busca de seu couro?",
        "answer": "Couro-já.",
    },
    {"question": "Qual é a Lua que nunca esta com fome?", "answer": "Lua cheia."},
    {
        "question": "O que tem cara de um lado e animal do outro?",
        "answer": "As notas.",
    },
    {
        "question": "Segunda pessoa do singular; Água passa; Qual é o nome do animal?",
        "answer": "TUcano.",
    },
    {
        "question": "Eu tenho um cachorro que se chama Choco. O que Choco faz?",
        "answer": "CHOCO-late.",
    },
    {
        "question": "Ge estava andando de bicicleta, mas ele não viu a ladeira que estava à sua frente. O que falaram para ele?",
        "answer": "Ge-Ladeira.",
    },
    {
        "question": "O que o tempo e a novela tem em comum?",
        "answer": "O tempo é o Senhor da Razão, e a novela é a Senhora do Destino.",
    },
    {
        "question": "Por que parente e igual a dente?",
        "answer": "Porque quanto mais afastado melhor pra não juntar sujeira.",
    },
    {"question": "Qual o país dos touros?", "answer": "Bull-Garia."},
    {"question": "Qual a cantora que abre todas as portas?", "answer": "Kelly Key."},
    {
        "question": "Por que os torcedores estavam com a mão na cara?",
        "answer": "Por que os atletas iam jogar tênis.",
    },
    {
        "question": "Por que as abelhas não comem pão de sal?",
        "answer": "Porque elas já têm o pão de mel.",
    },
    {
        "question": "Nas novelas, como fazer para os atores vovôs falarem mais alto?",
        "answer": "É só apertar o vô-lume.",
    },
    {
        "question": "Por que os camaleões mudam de cor sozinho?",
        "answer": "Porque eles não precisam de lápis de cor.",
    },
    {
        "question": "Qual a comida que tem um grupo de soldados prontos para guerra?",
        "answer": "Feijão Tropeiro.",
    },
    {
        "question": "Por que os baianos não deixam nada aberto?",
        "answer": "Porque eles tem o vatampá.",
    },
    {"question": "Qual o ator que mais gosta de flores?", "answer": "Tony Ramos."},
    {"question": "Qual a atriz mais enxuta?", "answer": "Deborah Secco."},
    {"question": "Qual o santo do Rodrigo?", "answer": "São Toro."},
    {
        "question": "Qual enfermidade tem o técnico da seleção brasileira de futebol quando entra em um labirinto?",
        "answer": "Labirin-Tite.",
    },
    {"question": "Qual o jogador que só vive com raiva?", "answer": "Bravo."},
    {
        "question": "O que todo homem faz quando está no banheiro?",
        "answer": "Sai do banheiro.",
    },
    {
        "question": "Por que o nadador jogou a televisão na piscina?",
        "answer": "Para fazer um nado sintonizado.",
    },
    {
        "question": "Por que o italiano tem que se equilibrar jogando xadrez?",
        "answer": "Porque senão ele perde sua torre.",
    },
    {
        "question": "Por que a cama do sabão facilmente estoura?",
        "answer": "Porque seu colchão é de espuma.",
    },
    {
        "question": "Qual é o eletrodoméstico preferido do Batman?",
        "answer": "Bat-deira.",
    },
    {"question": "Qual comida que quase tira um 10?", "answer": "Strogo-nove."},
    {"question": "Qual o brinquedo preferido do McDonald's?", "answer": "McSteel."},
    {
        "question": "O que a vaca foi fazer na papelaria?",
        "answer": "Comprar uma muuuuuuuu-chila.",
    },
    {
        "question": "Qual o material escolar que mostra a parte de seu corpo que dói?",
        "answer": "Aponta-dor.",
    },
    {"question": "Qual a rede social mais gorda?", "answer": "InstaGrama."},
    {
        "question": "Qual é o tipo de festa que os cegos frequentam?",
        "answer": "O braille funk.",
    },
    {
        "question": "Por que no Rio de Janeiro as pessoas não comem pão de sal?",
        "answer": "Porque eles têm o Pão de Açúcar.",
    },
    {"question": "Qual super herói tira foto no escuro?", "answer": "Flash."},
    {
        "question": "Quando está apaixonado, como um sabão em pó se declara?",
        "answer": "Eu te OMO.",
    },
]


def _dumps(obj):
    """Pretty JSON"""
    return json.dumps(obj, indent=4, sort_keys=True, ensure_ascii=False) + "\n"


async def get_random_joke(request):
    jk_idx = random.randint(0, len(PIADAS) - 1)

    jk = PIADAS[jk_idx]
    return web.json_response(jk, dumps=_dumps)


app = web.Application()
app.add_routes([web.get("/", get_random_joke)])
web.run_app(app, port=os.getenv("PORT", 5000))

