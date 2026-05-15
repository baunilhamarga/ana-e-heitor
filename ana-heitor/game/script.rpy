# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Personagens
define a = Character("Ana", color="#f0a7bb")
define h = Character("Heitor", color="#89c7f5")

# =========================
# PERSONAGENS - ANA
# =========================

image ana college neutral = im.Scale("ana college neutral.png", 600, 804)
image ana college happy = im.Scale("ana college happy.png", 600, 804)
image ana college super_happy = im.Scale("ana college super happy.png", 600, 804)
image ana college embarrassed = im.Scale("ana college embarrassed.png", 600, 804)
image ana college sad = im.Scale("ana college sad.png", 600, 804)
image ana college thinking = im.Scale("ana college thinking.png", 600, 804)
image ana college soft = im.Scale("ana college soft.png", 600, 804)
image ana college annoyed = im.Scale("ana college annoyed.png", 600, 804)
image ana college surprised = im.Scale("ana college surprised.png", 600, 804)
image cg kiss = im.Scale("bg kissing.png", 1920, 1080)

# =========================
# ANA - HOME
# =========================

image ana home neutral = im.Scale("ana home neutral.png", 600, 804)
image ana home soft = im.Scale("ana home soft.png", 600, 804)
image ana home happy = im.Scale("ana home happy.png", 600, 804)
image ana home embarrassed = im.Scale("ana home embarrassed.png", 600, 804)
image ana home sleepy = im.Scale("ana home sleepy.png", 600, 804)
image ana home sad = im.Scale("ana home sad.png", 600, 804)
image ana home emotional = im.Scale("ana home emotional.png", 600, 804)
image ana home serious = im.Scale("ana home serious.png", 600, 804)

# =========================
# ANA - PARTY / CASUAL
# =========================

image ana party neutral = im.Scale("ana party neutral.png", 600, 804)
image ana party happy = im.Scale("ana party happy.png", 600, 804)
image ana party super_happy = im.Scale("ana party super happy.png", 600, 804)
image ana party embarrassed = im.Scale("ana party embarrassed.png", 600, 804)
image ana party thinking = im.Scale("ana party thinking.png", 600, 804)
image ana party happy_hand = im.Scale("ana party happy hand.png", 600, 804)

image ana casual neutral = im.Scale("ana casual neutral.png", 600, 804)
image ana casual happy = im.Scale("ana casual happy.png", 600, 804)

# =========================
# ANA - TRIP
# =========================

image ana trip happy = im.Scale("ana trip happy.png", 600, 804)
image ana trip playful = im.Scale("ana trip playful.png", 600, 804)
image ana trip amazed = im.Scale("ana trip amazed.png", 600, 804)
image ana trip soft = im.Scale("ana trip soft.png", 600, 804)

# =========================
# HEITOR - COLLEGE
# =========================

image heitor college neutral = im.Scale("heitor college neutral.png", 600, 804)
image heitor college soft_smile = im.Scale("heitor college soft smile.png", 600, 804)
image heitor college amused = im.Scale("heitor college amused.png", 600, 804)
image heitor college surprised = im.Scale("heitor college surprised.png", 600, 804)
image heitor college serious = im.Scale("heitor college serious.png", 600, 804)
image heitor college thoughtful = im.Scale("heitor college thoughtful.png", 600, 804)
image heitor college shy_smile = im.Scale("heitor college shy smile.png", 600, 804)

# =========================
# HEITOR - HOME
# =========================

image heitor home neutral = im.Scale("heitor home neutral.png", 600, 804)
image heitor home soft_smile = im.Scale("heitor home soft smile.png", 600, 804)
image heitor home amused = im.Scale("heitor home amused.png", 600, 804)
image heitor home surprised = im.Scale("heitor home surprised.png", 600, 804)
image heitor home sleepy = im.Scale("heitor home sleepy.png", 600, 804)
image heitor home serious = im.Scale("heitor home serious.png", 600, 804)

# =========================
# HEITOR - OUTROS
# =========================

image heitor nervous = im.Scale("heitor nervous.png", 600, 804)
image heitor focused = im.Scale("heitor focused.png", 600, 804)
image heitor gentle = im.Scale("heitor gentle.png", 600, 804)
image heitor soft_laugh = im.Scale("heitor soft laugh.png", 600, 804)
image heitor tired_smile = im.Scale("heitor tired smile.png", 600, 804)
image heitor thoughtful = im.Scale("heitor thoughtful.png", 600, 804)

# =========================
# BACKGROUNDS
# =========================

image bg bandejao = im.Scale("bg bandejao.png", 1920, 1080)
image bg party = im.Scale("bg party.png", 1920, 1080)
image bg street_day = im.Scale("bg street day.png", 1920, 1080)
image bg bus_stop = im.Scale("bg bus stop.png", 1920, 1080)
image bg sushi = im.Scale("bg sushi.png", 1920, 1080)
image bg sala_game = im.Scale("bg sala game.png", 1920, 1080)
image bg sofa_series = im.Scale("bg sofa series.png", 1920, 1080)
image bg minas = im.Scale("bg minas.png", 1920, 1080)
image bg espirito_santo = im.Scale("bg espirito santo.png", 1920, 1080)
image bg festa = im.Scale("bg festa.png", 1920, 1080)
image bg desktop_code = im.Scale("bg desktop code.png", 1920, 1080)
image bg sofa_dim = im.Scale("bg sofa dim.png", 1920, 1080)

image bg ap_heitor_day = im.Scale("bg ap heitor day.png", 1920, 1080)
image bg ap_heitor_night = im.Scale("bg ap heitor night.png", 1920, 1080)
image bg airport = im.Scale("bg airport.png", 1920, 1080)
image bg bedroom_night = im.Scale("bg bedroom night.png", 1920, 1080)
image bg burger_place = im.Scale("bg burger_place.png", 1920, 1080)
image bg cafe_evening = im.Scale("bg cafe_evening.jpg", 1920, 1080)
image bg park_evening = im.Scale("bg park_evening.png", 1920, 1080)
image bg bus = im.Scale("bg bus.png", 1920, 1080)
image bg hamburgueria = im.Scale("bg hamburgueria.png", 1920, 1080)

# The game starts here.
label start:

    $ play_bgm("heitor_default")
    $ current_pov = "heitor"
    $ heitor_progress = 0
    $ ana_progress = 30
    $ heitor_money = 25
    $ ana_money = 200
    $ current_day = 1
    $ time_slot_index = 1
    $ current_country_label = "🇧🇷 Brasil"
    $ special_day_label = ""
    $ first_kiss_done = False
    $ career_phase = "btg"
    $ set_love_cap_stage("intro")
    $ unlocked_locations = ["poli", "bandejao", "heitor_home", "shop", "work"]
    $ completed_memories = []
    $ inventory = []
    $ mother_money_day = 0
    $ mother_money_requests_today = 0

    show screen relationship_hud
    call change_pov("heitor", "Uma rara ida ao Bandejão Central") from _call_change_pov_1

    scene bg bandejao
    with fade

    pause 1.0

    show heitor college neutral at pov_left

    show ana college neutral at other_right

    pause 0.5

    a "Engraçado… a gente é da mesma sala há meses."

    pause 0.4

    show heitor college soft_smile

    h "Eu sei… eu só… sou mais quieto."

    pause 0.3

    show ana college happy

    a "Eu percebi."

    a "Mas hoje você tá falando mais."

    show heitor college amused

    h "Você fala por nós dois."

    show ana college embarrassed

    a "Eu falo demais quando fico confortável."

    show heitor college soft_smile

    h "Então eu vou considerar isso um elogio."

    show ana college super_happy

    a "Pode considerar."

    $ advance_dialog_section("primeiro papo")

    pause 1.0

    show ana college thinking

    a "O que você gosta de fazer?"

    show ana college neutral

    menu:
        "Calistenia":

            show heitor college amused

            h "Gosto muito de praticar calistenia."

            show ana college surprised

            a "Ah, que legal."

            show ana college embarrassed

            a "Eu gosto mais de academia… não consigo fazer essas coisas não."

            show heitor college soft_smile

            h "Consegue sim. É questão de praticar."

            h "Todo mundo começa ruim."

            $ add_love(3, "calistenia", person="ana")

        "Street Fighter":

            show heitor college amused

            h "Gosto muito de jogar."

            h "Principalmente jogos de luta. O meu preferido é Street Fighter. Conhece?"

            show ana college thinking

            a "Acho que não…"

            $ queue_notification("{color=%s}O que é um Street Fighter? É de comer?{/color}" % pov_color("ana"))

            show ana college embarrassed

            a "Não gosto muito de jogar."

            show heitor college soft_smile

            h "Quais você já tentou?"

            a "Não muitos."

            a "Sou um desastre com quase todo jogo."

            h "Podíamos jogar juntos se quiser..."

            show ana college embarrassed

        "Desenhar":

            show heitor college soft_smile

            h "Gosto muito de desenhar no meu tempo livre."

            show ana college surprised

            a "Sério?"

            show ana college embarrassed

            a "Eu já pintei quando era criança…"

            a "Mas hoje em dia não consigo desenhar nem uma porta."

            a "Sou horrível."

            show heitor college amused

            h "Duvido."

            $ add_love(2, "desenhar", person="ana")

    $ advance_dialog_section("gostos e hobbies")

    show ana college happy

    a "Mas bom…"

    a "O que mais você gosta de fazer?"

    show ana college happy

    a "E o que você gosta de comer?"

    show ana college annoyed

    a "Com certeza não é nada aqui do bandejão."

    a "Isso aqui é simplesmente horrível."

    show heitor college amused

    a "Juro que teve uma vez que eu quase passei mal."

    show ana college thinking

    a "O do central é o menos pior."

    a "Qual bandejão você gosta mais?"

    menu:

        "Física":

            show heitor college thoughtful

            h "O da Física com certeza."

            show ana college surprised

            a "Sério??"

            show ana college happy

            a "Você é a primeira pessoa que eu vejo dizendo isso."

            $ add_love(1, "bandejão da Física", person="ana")

        "Central":

            show heitor college soft_smile

            h "O Central."

            show ana college super_happy

            a "EU SABIA."

            a "O Central é claramente o melhor."

            $ add_love(3, "bandejão Central", person="ana")

        "Química":

            show heitor college amused

            h "O da Química."

            show ana college thinking

            a "Hmm…"

            show ana college happy

            a "Ok, esse eu aceito."

            a "Mas depende muito do dia."

            $ add_love(2, "bandejão da Química", person="ana")

    $ advance_dialog_section("ranking do bandejão")

    pause 0.8

    show ana college embarrassed

    a "Eu avisei que falo demais."

    show heitor college soft_smile

    h "Eu não estou reclamando."

    pause 1.5

    show ana college soft
    hide ana
    hide heitor

    scene black
    with dissolve

    call change_pov("ana", "Depois do bandejão") from _call_change_pov_2

    show ana college thinking at pov_left

    pause 1.2

    ana_thought "Ficamos conversando o jantar inteiro. Me dissociei um pouco dos arredores."

    ana_thought "Todos os amigos conversavam entre si, mas havia algo me impedindo de olhar em outra direção."

    pause 1.0
    ana_thought "Eu fiquei um pouco intrigada. Havia muito tempo que não sentia nada assim. Bom, não me leve a mal, mas eu estava em uma situação bem ruim havia muito tempo." 
    ana_thought "Eu me via andando por aí sem rumo, sem objetivo, sem interagir tanto. Eu me via uma pessoa completamente da que eu era antes e isso me assustava um pouco."
    ana_thought "De uns meses para cá isso mudou, eu pude sentir essa mudança na forma como eu conversava, em como eu agia. Talvez eu devesse dar uma chance para nos tornarmos amigos."
    ana_thought "Talvez um pouco mais. Ele era tão fofo..."
    pause 1.2
    ana_thought "Ai Ana, você pensa demais. Um homem de 24 anos nunca teria interesse em uma pirralha como você."
    ana_thought "Ótimo. Diagnóstico feito com zero dados e cem por cento de convicção."

    $ advance_dialog_section("primeira conversa no bandejão")
    if endgame_replay_mode:
        return
    call free_time_phase("primeiro_contato") from _call_free_time_phase_1

    jump raio_x

label raio_x:

    $ play_bgm("ana_default")
    scene bg bedroom_night
    with fade

    show ana casual neutral at pov_left

    ana_thought "Cheguei em casa e não sabia o que mandar."

    menu:
        "Mandar um oi normal.":
            jump mensagem_normal
        "Mandar algo completamente idiota.":
            jump mensagem_raiox

label mensagem_raiox:

    scene bg bedroom_night
    with fade

    show ana home sad at pov_left

    ana_thought "Eu mandei a coisa mais idiota possível."

    pause 0.5

    ana_thought "Uma foto do meu raio-x."

    pause 0.8

    call whatsapp_raiox_excerpt from _call_whatsapp_raiox_excerpt

    pause 0.5

    show ana home happy

    ana_thought "Nossa, eu sou burra!"

    show ana home embarrassed

    ana_thought "Achei que tinha sido completamente inconveniente."

    pause 0.5

    show ana home soft

    ana_thought "Mas ele não pareceu se importar."

    pause 1.2

    scene black
    with fade

    show ana home soft at pov_left

    ana_thought "E a conversa continuou por vários dias."

    pause 1.0
    ana_thought "Ele não notava meu tom um pouco mais sugestivo em algumas mensagens. Isso me deixava um pouco pensativa demais. Não sei o porquê..."

    heitor_thought "Ela mandou um raio-x como primeira grande mensagem. Eu devia ter percebido que isso era o começo de uma saga."

    $ set_love_cap_stage("mensagens_iniciais")
    $ add_love(5, "mensagens iniciais")
    if endgame_replay_mode:
        return
    call free_time_phase("mensagens_iniciais") from _call_free_time_phase_2

    hide ana
    pause 1.0
    jump picles

label mensagem_normal:

    show ana casual happy

    a "Oi :)"

    show heitor college neutral at other_right

    h "Oi."

    show ana casual neutral

    ana_thought "Sem graça."

    ana_thought "Eu devia ter mandado algo diferente."

    scene black
    with fade

    $ set_love_cap_stage("mensagens_iniciais")
    $ add_love(3, "oi estrategicamente simples")
    if endgame_replay_mode:
        return
    call free_time_phase("mensagens_iniciais") from _call_free_time_phase_3

    jump picles

label picles:

    $ play_bgm("date_fun")
    scene bg party
    with fade

    pause 1.0

    show ana party neutral at pov_left

    show heitor college neutral at other_right

    ana_thought "Eu convidei ele e os meninos pro Picles."

    ana_thought "Ele odiou."

    hide ana
    hide heitor
    call quick_change_pov("heitor") from _call_quick_change_pov_1
    show heitor college neutral at pov_left
    show ana party neutral at other_right

    heitor_thought "Ei, quem disse que eu odiei?"

    hide ana
    hide heitor
    call quick_change_pov("ana") from _call_quick_change_pov_2
    show ana party neutral at pov_left
    show heitor college neutral at other_right

    show ana party embarrassed

    ana_thought "Mas também… o que que eu tava pensando."

    ana_thought "Ele e o Solano odeiam lugares muito cheios."

    ana_thought "Devia ter pensado em outra coisa."

    show heitor college serious

    h "Tá muito barulhento."

    show ana party happy

    ana_thought "Eu achei fofo ele reclamar."

    ana_thought "Eu acho tudo nele fofo."

    ana_thought "Ai Ana, para, você não pode encarar as coisas dessa forma."

    show ana party thinking

    ana_thought "Mas que merda… eu errei feio mesmo."

    a "Acho que podemos fazer alguma outra coisa."

    menu:

        "Ir numa hamburgueria (R$ 50,00)" if current_money() >= 50:

            $ spend_money(50, "hamburgueria")

            scene bg burger_place
            with fade

            pause 1.0

            show ana college happy at pov_left

            show heitor college soft_smile at other_right

            pause 0.5

            ana_thought "A gente acabou indo numa hamburgueria."

            ana_thought "Bem mais quieta."

            h "Aqui é melhor."

            show ana college happy

            a "Eu sabia que comida ia resolver."

            pause 0.8

            show ana college embarrassed

            show heitor college soft_smile

            pause 1.0

            ana_thought "A gente passou alguns segundos em silêncio."

            pause 1.0

            ana_thought "Com a cabeça deitada na mesa."

            pause 2.5

            show ana college sad

            ana_thought "Eu quase morri de vergonha."

            $ add_love(5, "hamburgueria mais tranquila", person="ana")
            $ add_love(5, "hamburgueria mais tranquila", person="heitor")

            scene black
            with fade

            if endgame_replay_mode:
                return
            jump ep_yoshi


        "Ir comer qualquer coisa (R$ 25,00)" if current_money() >= 25:

            $ spend_money(25, "lanche improvisado")

            scene bg cafe_evening
            with fade

            show ana college happy at pov_left

            show heitor college soft_smile at other_right

            ana_thought "A gente decidiu procurar alguma coisa pra comer."

            h "Muito melhor que lá."

            show ana college happy

            ana_thought "Ele disse que gostou…"

            show ana college thinking

            ana_thought "Mas não sei não."

            a "Esse lugar é meio sem graça."

            $ add_love(2, "lanche improvisado", person="ana")
            $ add_love(2, "lanche improvisado", person="heitor")

            scene black
            with fade

            if endgame_replay_mode:
                return
            jump ep_yoshi


        "Dar uma volta no parque":

            scene bg park_evening
            with fade

            show ana college happy at pov_left

            show heitor college soft_smile at other_right

            ana_thought "A gente resolveu só dar uma volta."

            ana_thought "O parque tava bem tranquilo…"

            show ana college thinking

            ana_thought "Mas tenho um pouco de medo."

            ana_thought "Aqui em São Paulo é muito perigoso."

            h "Assim é perfeito."

            show ana college soft

            ana_thought "Eu acho que ele gosta mesmo é de paz."

            $ add_love(2, "volta no parque", person="ana")
            $ add_love(2, "volta no parque", person="heitor")

            scene black
            with fade

            if endgame_replay_mode:
                return
            jump ep_yoshi

label ep_yoshi:

    $ play_bgm("study_debug")
    scene bg ap_heitor_day
    with fade

    show ana college neutral at pov_left

    show heitor college shy_smile at other_right

    ana_thought "Eu aceitei sair com ele, mas era o último dia antes de uma tarefa importante."

    a "Mas só se terminasse o EP do Yoshi."

    h "Prometo. Se a gente terminar, eu te levo pra passear."

    show ana college happy

    a "Fechado."

    scene bg desktop_code
    with dissolve

    show ana college neutral at pov_left

    show heitor focused at other_right

    ana_thought "Eu não tava entendendo absolutamente nada."

    h "Aqui você cria a função... depois chama ela dentro do loop."

    pause 0.5

    show ana college embarrassed

    a "Mas… para quê esse loop? Isso não faz sentido nenhum!"

    show heitor soft_laugh

    h "Tá tudo bem."

    h "Eu explico de novo."

    pause 1.0

    ana_thought "Eu praticamente não fiz nada."

    show ana college sad

    ana_thought "Eu fiquei me sentindo inútil."

    show heitor gentle

    h "Você não precisa saber disso tudo agora. Eu gosto muito do Yoshi, mas o pessoal acha a matéria dele bem difícil."

    h "A gente aprende junto."

    pause 1.5

    scene bg ap_heitor_night
    with fade

    show ana college neutral at pov_left

    show heitor tired_smile at other_right

    h "Terminamos."

    a "Você fez quase tudo, eu fiquei conversando com você e com seus vizinhos, estou me sentindo muito culpada. E outra, não podemos enviar a mesma coisa, ele não vai aceitar."

    h "Relaxa."

    pause 1.0

    scene bg sofa_dim
    with dissolve

    show ana college neutral at pov_left

    show heitor thoughtful at other_right

    ana_thought "A gente colocou um anime pra assistir. Eu não entendi nada. Eu olhava um pouco para baixo o tempo todo, com medo de levantar a cabeça, de falar alguma bobagem ou fazer algo errado."
    ana_thought "Não sei porque eu ficava tão nervosa na presença dele. Até aquele momento parecia tudo muito natural, mas o fato de ele ter me chamado para sair me deixou um pouco confusa."
    ana_thought "Afinal, faria sentido dois amigos saírem sozinhos dessa forma?"

    pause 1.0

    show ana college embarrassed

    ana_thought "Ele estava sentado no sofá. Ele também não olhava para mim. A gente jogava conversa fora aqui e ali, mas eu mal conseguia me concentrar no filme."

    pause 1.5

    ana_thought "Em alguns momentos ele sorria de uma maneira tão genuína, com umas conversas tão bobas." 
    ana_thought "Se fosse qualquer outra pessoa eu acharia normal, mas ele era tão fechado, não o via sorrindo com quase ninguém. O sorriso era lindo, um dos mais lindos que já vi na minha vida."
    ana_thought "Não que eu fosse dizer algo para ele. Eu não sou nem louca."

    pause 1.0

    show heitor thoughtful

    ana_thought "Me perguntei se seríamos somente amigos mesmo. Fiquei esperando a noite inteira para que ele dissesse algo."

    pause 2.0

    $ duck_music()
    show ana college sad

    ana_thought "Mas nada aconteceu."

    pause 2.0

    scene black
    with fade

    show ana college sad at pov_left

    ana_thought "Eu fui embora e me esqueci desse assunto. Nada nunca aconteceria entre a gente."

    hide ana
    $ restore_music()

    jump mensagem_onibus

label mensagem_onibus:

    $ play_bgm("ana_sad")
    scene bg bus
    with fade

    pause 1.0

    show ana home sleepy at pov_left

    ana_thought "Eu entrei no ônibus e já me posicionei para dormir, mesmo sabendo que eu não iria dormir nada."

    pause 0.8

    ana_thought "Não me leve a mal, eu amo dormir, mas minhas costas doem muito a noite, principalmente sem conseguir deitar."

    pause 1.0

    show ana home neutral

    ana_thought "Era o último dia para entregar o trabalho do ep."

    pause 0.6

    show ana home sad

    ana_thought "Eu não ia mais enviar, acho que não dava tempo mais e eu também não enviaria algo repetido."

    pause 1.2

    ana_thought "Eu fui olhar as mensagens mais uma vez e talvez agradecer ao Heitor pelo tempo, mesmo que tenha sido somente entre amigos."

    pause 1.5

    scene black
    with dissolve

    show ana home neutral at pov_left

    pause 0.8

    ana_thought "Mas assim que abri as mensagens dei de cara com uma mensagem dele:"

    hide ana

    pause 1.0

    scene bg bus
    with fade

    show heitor home soft_smile at other_right:
        xzoom -1

    pause 0.5

    h "Eu fiz uma versão do ep para você."

    pause 1.5

    show ana home embarrassed at pov_left

    ana_thought "Assim que eu abri tinha tudo, era completamente diferente da dele, um código completamente novo, tinha o cabeçalho, meu nusp, nome completo."

    pause 1.2

    ana_thought "Eu passei 3 minutos somente lendo de novo para ter certeza do que estava vendo."

    pause 2.0

    show ana home soft

    ana_thought "Acho que ninguém tinha feito algum trabalho por mim, em troca de nada, só para ajudar."

    pause 1.2

    ana_thought "Caramba."

    pause 0.8

    show ana home emotional

    ana_thought "Ele é um bom amigo e uma pessoa maravilhosa."

    pause 1.5

    ana_thought "Vou agradecer."

    pause 1.0

    menu:

        "Agradecer de forma simples":

            show ana home neutral

            a "Obrigada, de verdade."

            pause 0.5

            show ana home embarrassed

            a "Você não precisava ter feito isso, até meu nusp você encontrou, não sei como."

            pause 1.0

            show heitor home soft_smile at other_right:
                xzoom -1

            h "Fica tranquila."

            pause 1.0

        "Falar tudo que está sentindo":

            show ana home emotional

            a "Eu nem sei o que dizer."

            pause 0.5

            a "Ninguém nunca fez algo assim por mim."

            pause 0.8

            show ana home embarrassed

            a "Obrigada, de verdade."

            pause 1.0

            show heitor home soft_smile at other_right:
                xzoom -1

            h "Fico feliz em ajudar."

            pause 1.0

    $ set_love_cap_stage("ep_yoshi")
    $ add_love(8, "EP salvo na madrugada")
    if endgame_replay_mode:
        return
    call free_time_phase("primeiro_beijo", 24, "heitor") from _call_free_time_phase_4

label primeiro_beijo:
    $ first_kiss_done = True
    $ play_bgm("romance_soft")

    pause 1.5

    scene bg bandejao
    with fade

    show ana college neutral at pov_left
    show heitor college neutral at other_right

    pause 1.5

    h "Você vai perder o ônibus."

    pause 0.5

    a "Ainda dá tempo. Eu preciso chegar em casa para assistir essa aula e estudar."

    pause 0.8

    scene bg street_day
    with fade

    pause 1.0

    show ana college neutral at pov_left

    show heitor college neutral at other_right

    ana_thought "A gente foi conversando do bandejão até o ponto."

    pause 0.8

    ana_thought "Eu estava muito preocupada com a monitoria e o Heitor parecia não estar nenhum pouco preocupado."

    pause 1.2

    scene bg bus_stop
    with fade

    pause 1.0

    show ana college neutral at pov_left

    show heitor college neutral at other_right

    ana_thought "Até que quando chegamos no ponto e nos sentamos eu peguei o meu celular e comecei a ver."

    pause 0.8

    show ana college thinking

    ana_thought "Eu não consegui prestar atenção."

    pause 1.2

    ana_thought "Eu me virei e o Heitor estava me olhando também."

    pause 1.5

    show ana college embarrassed

    ana_thought "Eu fiquei um pouco nervosa, não sabia muito bem o que pensar."

    pause 1.2

    ana_thought "Não tinha ninguém perto, a rua completamente vazia e o ônibus não chegava de jeito nenhum."

    pause 1.5

    show ana college soft

    ana_thought "Eu encostei a minha cabeça no ombro dele, só por um instante."

    pause 1.5

    ana_thought "Não sei de onde tirei tanta coragem, mas eu me senti segura em fazer isso."

    pause 1.5

    ana_thought "Eu tinha um pouco de medo, de estar com algum homem sozinha, num lugar sem ninguém, mas eu já me sentia muito confortável perto dele, era incapaz de fazer mal a uma mosca."

    pause 2.0

    ana_thought "Quando eu olhava para o lado, ele estava olhando também, eu morria de vergonha, minha bochecha corava e eu tentava voltar a ver a aula."

    pause 2.0

    show heitor college soft_smile

    pause 1.0

    ana_thought "Ele me olhou, tirou o celular da minha mão e me beijou, eu escutei o celular dele caindo no chão e paramos por um instante."

    pause 2.5

    scene bg bus_stop
    show cg kiss
    with dissolve

    pause 3.0

    hide cg kiss
    with dissolve

    scene black
    with dissolve

    show ana college soft at pov_left

    pause 1.5

    ana_thought "Foi lindo, eu me esqueci de tudo, das aulas, do ônibus."

    pause 1.5

    ana_thought "Meu Deus, o ônibus!"

    pause 1.2

    scene bg bus_stop
    with fade

    pause 1.0

    show ana college surprised at pov_left

    show heitor college surprised at other_right

    ana_thought "O ônibus para a casa dele chegou e a gente parou de se beijar."

    pause 1.5

    show ana college thinking

    ana_thought "Eu olhei para ele e pensei: por que não?"

    pause 1.5

    show ana college happy

    a "vou para a sua casa, eu não tenho nada melhor para fazer mesmo!"

    pause 1.0

    show heitor college soft_smile

    pause 1.0

    ana_thought "Ele olhou para mim sorrindo, pegou na minha mão e entramos no ônibus juntos."

    pause 1.5

    scene bg bus
    with fade

    pause 1.5

    ana_thought "A partir desse dia a gente não se desgrudou mais. Eu acho que já estava apaixonada e nem percebia."

    pause 2.0

    scene black
    with fade

    show ana college happy at pov_left

    pause 2.0

    hide ana

    $ set_love_cap_stage("pedido_namoro")
    $ add_love(10, "primeiro beijo")
    $ add_love(24, "primeiro beijo", person="heitor")
    $ unlock_achievement("first_kiss")
    if endgame_replay_mode:
        return
    call change_pov("heitor", "Preparando o pedido") from _call_change_pov_3
    call free_time_phase("pedido_namoro") from _call_free_time_phase_5

    jump pedido_namoro

label pedido_namoro:
    $ current_pov = "heitor"
    $ play_bgm("choice_tension")

    scene bg hamburgueria
    with fade

    pause 1.0

    show heitor nervous at pov_left
    show ana college happy at other_right

    pause 0.5

    heitor_thought "Duas semanas depois do primeiro beijo…"

    pause 1.0

    heitor_thought "Eu chamei ela pra ir numa hamburgueria."

    pause 1.2

    h "Você quer batata também?"

    pause 0.4

    a "Sempre."

    pause 1.8

    show heitor nervous

    pause 0.8

    call quick_change_pov("ana") from _call_quick_change_pov_3
    show ana college happy at pov_left
    show heitor nervous at other_right

    ana_thought "Ele tava estranho."

    pause 0.8

    ana_thought "Quieto demais."

    pause 1.2

    call quick_change_pov("heitor") from _call_quick_change_pov_4
    show heitor nervous at pov_left
    show ana college neutral
    show ana college neutral at other_right

    a "Você tá bem?"

    pause 1.2

    show heitor nervous

    h "Tô."

    pause 1.2

    h "Na verdade…"

    pause 2.5

    show heitor nervous

    pause 0.8

    h "Eu comprei uma coisa pra você."

    pause 1.0

    show ana college embarrassed

    a "Heitor…"

    pause 1.2

    h "Não é nada demais."

    pause 0.8

    h "Só…"

    pause 1.8

    h "Um par de brincos."

    pause 0.6

    h "E uns chocolates da Cacau Show."

    pause 1.5

    show ana college super_happy

    a "Você é muito fofo."

    pause 2.0

    call quick_change_pov("ana") from _call_quick_change_pov_5
    show ana college super_happy at pov_left
    show heitor nervous at other_right

    ana_thought "Eu já sabia o que era, afinal tínhamos conversado sobre isso e eu disse que aceitaria caso ele me pedisse do jeito certo." 
    ana_thought "Mas sendo honesta, qualquer pedido seria perfeito. Ele era perfeito."

    pause 2.0

    call quick_change_pov("heitor") from _call_quick_change_pov_6
    show heitor nervous
    show heitor nervous at pov_left
    show ana college super_happy at other_right

    pause 1.0

    h "Ana…"

    pause 2.0

    h "Quer namorar comigo?"

    pause 2.5

    call quick_change_pov("ana") from _call_quick_change_pov_7
    show ana college super_happy at pov_left
    show heitor nervous at other_right

    $ duck_music()
    menu:
        "Eu já estava esperando isso.":

            show ana college happy

            a "Demorou, hein?"

            pause 1.0

            jump aceita_namoro

        "Claro que eu quero.":

            show ana college super_happy

            a "Claro que eu quero."

            pause 1.0

            jump aceita_namoro

        "Eu achei que você nunca ia pedir.":

            show ana college embarrassed

            a "Eu achei que você nunca ia pedir."

            pause 1.0

            jump aceita_namoro


label aceita_namoro:

    $ restore_music()
    $ dating_started = True
    $ play_bgm("romance_soft")

    call quick_change_pov("heitor") from _call_quick_change_pov_8
    show heitor nervous
    show heitor nervous at pov_left
    show ana college super_happy at other_right

    pause 1.0

    h "Então… isso é um sim?"

    pause 1.0

    call quick_change_pov("ana") from _call_quick_change_pov_9
    show ana college super_happy
    show ana college super_happy at pov_left
    show heitor nervous at other_right

    a "É óbvio que é um sim."

    pause 2.5

    scene bg hamburgueria
    with dissolve

    pause 1.0

    ana_thought "Eu saí daquela hamburgueria com brincos novos."

    pause 1.0

    ana_thought "Chocolate."

    pause 1.2

    ana_thought "E um namorado."

    pause 2.5

    scene black
    with fade

    $ duck_music()
    show ana college super_happy at pov_left

    pause 1.5

    ana_thought "E eu nunca me senti tão feliz."

    pause 2.0

    hide ana

    $ restore_music()
    $ set_love_cap_stage("primeiro_eu_te_amo")
    $ add_love(12, "pedido de namoro")
    $ unlock_achievement("dating_started")
    if endgame_replay_mode:
        return
    call change_pov("ana", "Namoro oficial") from _call_change_pov_4
    call relationship_gate("primeiro_eu_te_amo", 55, "O namoro começou. Agora vem a parte em que o carinho deixa de ser evento raro e vira rotina.") from _call_relationship_gate

    jump primeiro_eu_te_amo

label primeiro_eu_te_amo:

    $ play_bgm("romance_soft")
    scene bg ap_heitor_night
    with fade

    pause 1.5

    show ana college neutral at pov_left

    show heitor college soft_smile at other_right

    pause 1.0

    ana_thought "Estávamos com olhares fixos um no outro, depois de muito tempo juntos, muitas saídas, muitos beijos, abraços e muito carinho." 
    ana_thought "Eu já não conseguia desviar o olhar. Quando não me atentava aos seus olhos, estava apreciando seu sorriso, suas bochechas, seu nariz, seu cabelo. Tudo era lindo, como ele era lindo!" 
    ana_thought "Ele era tão gentil, tão carinhoso. Ele sempre fazia o que era moralmente correto, sempre pensava no bem das pessoas, mas acima de tudo parecia sempre estar pensando no meu bem."
    ana_thought "Ele era inteligente, educado. Era tão relaxante passar tempo com ele, parecia que eu não tinha que fingir ser alguém que eu não era. Podia ficar triste, feliz, boba; ele gostava de todas as versões."

    pause 2.5

    show ana college embarrassed

    pause 0.8

    $ duck_music()
    ana_thought "Eu comecei a pensar."

    pause 1.0

    ana_thought "Será que já era isso?"

    pause 2.0

    show heitor college neutral

    pause 0.8

    $ restore_music()
    h "O que foi?"

    pause 1.2

    show ana college neutral

    a "Posso te perguntar uma coisa?"

    pause 0.8

    h "Pode."

    pause 2.5

    show ana college embarrassed

    a "Ainda tá muito cedo pra dizer que eu te amo?"

    pause 3.0

    show heitor college surprised

    pause 1.5

    show heitor college soft_smile

    pause 1.2

    h "Não."

    pause 1.5

    h "Porque eu também te amo."

    $ restore_music()
    pause 3.5

    show ana college super_happy

    pause 1.0

    ana_thought "Foi simples."

    pause 1.0

    ana_thought "Sem discurso."

    pause 1.0

    ana_thought "Sem preparação."

    pause 2.0

    ana_thought "Mas foi o momento em que eu soube."

    pause 2.5

    scene black
    with fade

    show ana college super_happy at pov_left

    pause 1.5

    $ duck_music()
    ana_thought "Não era cedo."

    pause 1.2

    ana_thought "Era exatamente a hora certa."

    pause 2.0

    $ restore_music()
    call whatsapp_te_amo_excerpt from _call_whatsapp_te_amo_excerpt

    hide ana

    $ set_love_cap_stage("australia")
    $ add_love(12, "primeiro eu te amo")
    $ unlock_achievement("first_love")
    if endgame_replay_mode:
        return

    jump ano_feliz

label ano_feliz:

    $ play_bgm("funny_win")
    scene black
    with fade

    ana_thought "Depois disso…"

    ana_thought "A gente viveu um ano inteiro muito feliz."

    ana_thought "E eu queria guardar cada memória."

    scene bg ap_heitor_night
    with dissolve

    show ana college happy at pov_left

    menu:
        "🎮 Jogar juntos":
            jump jogar_juntos

        "📺 Ver série juntos":
            jump ver_series

        "🍣 Jantar especial":
            jump jantar_sushi

        "👨‍👩‍👧 Visitar família":
            jump visitar_familia

        "🎉 Festa de formatura":
            jump festa_formatura

        "Continuar...":
            if endgame_replay_mode:
                return
            call relationship_gate("australia", 78, "Antes da Austrália, vale guardar mais algumas memórias do primeiro ano juntos.") from _call_relationship_gate_1
            jump preparando_mala

    scene bg ap_heitor_night
    with fade

    show ana college soft at pov_left

    ana_thought "Eu achava que nada podia mudar."

    ana_thought "E talvez…"

    ana_thought "Eu só não soubesse ainda o quanto amar também exige coragem."

    hide ana

    if endgame_replay_mode:
        return
    call relationship_gate("australia", 78, "Antes da Austrália, vale guardar mais algumas memórias do primeiro ano juntos.") from _call_relationship_gate_2

    jump preparando_mala

label jogar_juntos:

    $ complete_memory("jogar_juntos", love=5)
    $ play_bgm("date_fun")

    scene bg sala_game
    with fade

    show ana college happy at pov_left

    show heitor focused at other_right

    ana_thought "Nosso primeiro jogo completo juntos."

    a "It Takes Two."

    show ana college super_happy

    ana_thought "Eu gritava."

    ana_thought "Ele tentava manter a calma."

    h "Pula! Pula agora!"

    a "EU TÔ PULANDO!"

    pause 1.5

    ana_thought "Eu ria mais do que jogava, mas ele estava sempre muito paciente comigo."

    if endgame_replay_mode:
        return
    jump ano_feliz

label ver_series:

    $ complete_memory("ver_series", love=5)
    $ play_bgm("daily_light")

    scene bg sofa_series
    with fade

    show ana college neutral at pov_left

    show heitor college soft_smile at other_right

    menu:
        "Começar Breaking Bad":
            ana_thought "A gente ficou obcecado."
            ana_thought "Eu perguntava mil coisas."
            h "Confia no roteiro."
        "Ver Two and a Half Men":
            show ana college happy
            ana_thought "A gente ria de coisas idiotas."
            h "Esse é o ponto."

    pause 1.5

    ana_thought "Era simples."

    ana_thought "Mas era nosso."

    if endgame_replay_mode:
        return
    jump ano_feliz

label jantar_sushi:

    $ complete_memory("jantar_sushi", love=6)
    $ play_bgm("romance_soft")

    scene bg sushi
    with fade

    show ana college super_happy at pov_left

    show heitor college soft_smile at other_right

    ana_thought "A gente começou a sair pra comer sushi."

    ana_thought "Eu comia todo o peixe cru e ele comia todo o camarão."

    h "Esse aqui você gosta."

    a "Eu gosto porque você escolheu."

    pause 1.5

    if endgame_replay_mode:
        return
    jump ano_feliz

label visitar_familia:

    $ complete_memory("visitar_familia", love=7)
    $ play_bgm("daily_light")

    menu:
        "Minas":
            scene bg minas
            with fade
            show ana college happy at pov_left
            show heitor college shy_smile at other_right
            ana_thought "Ele conheceu meus pais."
            ana_thought "Eu fiquei nervosa o tempo inteiro."
        "Espírito Santo":
            scene bg espirito_santo
            with fade
            show ana college neutral at pov_left
            show heitor college soft_smile at other_right
            ana_thought "Eu conheci os pais dele."
            ana_thought "Eu queria causar uma boa impressão."

    pause 1.5

    if endgame_replay_mode:
        return
    jump ano_feliz

label festa_formatura:

    $ complete_memory("festa_formatura", love=7)
    $ play_bgm("funny_win")

    scene bg festa
    with fade

    show ana party super_happy at pov_left

    show heitor college amused at other_right

    ana_thought "A festa do Cecato foi incrível."

    ana_thought "A gente dançou a noite inteira, e o Heitor parecia estar tão feliz. Tiramos fotos lindas juntos, tudo foi lindo."

    show ana party happy_hand

    ana_thought "Eu nunca tinha me sentido tão leve."

    pause 1.5

    if endgame_replay_mode:
        return
    jump ano_feliz

label preparando_mala:

    call change_pov("heitor", "A mala para a Austrália") from _call_change_pov_5
    $ play_bgm("ana_sad")

    scene bg ap_heitor_day
    with fade

    show heitor home soft_smile at pov_left
    show ana home neutral at other_right

    a "Caramba, você vai levar isso tudo?"

    h "Eu vou mudar de país."

    a "Obrigada por me lembrar."

    h "É só um tempo."

    pause 1.5

    show ana home soft at other_right
    a "Quanto tempo é 'um tempo'?"

    show heitor home soft_smile at pov_left
    h "O suficiente pra eu sentir saudade."

    pause 2.0

    show ana home embarrassed at other_right
    a "Eu já tô sentindo."

    pause 2.5

    show ana home soft at other_right
    a "Eu não gosto dessa parte."

    show heitor home soft_smile at pov_left
    pause 1.5

    h "Eu sei."

    pause 2.5

    show heitor home soft_smile at pov_left
    h "Mas eu volto."

    pause 1.5

    show ana home sad at other_right
    a "Promete?"

    pause 1.5

    show heitor home serious at pov_left
    h "Prometo."

    pause 2.0

    scene black
    with fade

    call quick_change_pov("ana") from _call_quick_change_pov_10
    show ana home sad at other_right

    ana_thought "A mala ficou pronta."

    ana_thought "Mas nenhuma das duas pessoas ali estava."

    pause 2.0

    hide ana

    jump despedida_aeroporto

label despedida_aeroporto:

    call change_pov("ana", "Aeroporto: modo coração apertado") from _call_change_pov_6
    $ play_bgm("airport_tension")
    $ current_country_label = "🇧🇷 Brasil"

    scene bg airport
    with fade

    show ana home neutral at pov_left
    show heitor home soft_smile at other_right

    pause 2.0

    a "Eu odeio aeroporto."

    h "Eu sei, minha lindinha."

    pause 2.5

    show ana home soft at pov_left
    a "Não fala assim."

    h "Assim como?"

    a "Como se tivesse tudo normal."

    pause 2.0

    show heitor home soft_smile at other_right
    h "Mas é."

    h "É só um voo."

    pause 2.0

    show ana home serious at pov_left
    a "É um voo muito longo."

    pause 2.5

    show heitor home soft_smile at other_right
    h "Ei."

    pause 1.5

    show heitor home soft_smile at other_right
    h "Olha pra mim."

    pause 2.0

    show ana home soft at pov_left
    pause 2.0

    h "Você acha mesmo que eu ia deixar minha lindinha assim?"

    pause 2.5

    show ana home embarrassed at pov_left
    a "Eu não gosto quando você usa isso em momentos sérios."

    h "Eu uso porque é sério."

    pause 3.0

    "Atenção passageiros do voo 302..."

    pause 2.0

    show heitor home serious at other_right
    h "É o meu."

    pause 2.5

    show ana home sad at pov_left
    a "Amor, eu não quero que você vá embora, eu vou ficar muito sozinha..."

    pause 3.0

    h "Você vai me visitar, e eu vou te visitar quando puder e a gente vai fazer dar certo."

    h "Eu escolhi você para passar o resto da minha vida, eu não vou te deixar, não vou te largar nenhum momento e nós vamos passar por isso juntos."

    a "Promete?"

    show heitor home soft_smile at other_right
    h "Prometo."

    pause 2.5

    h "Cuida de você, pode me ligar quando quiser."

    pause 1.5

    show ana home soft at pov_left
    a "Você também, amor."

    pause 3.0

    h "Eu amo você, minha lindinha."

    pause 3.5

    show ana home sad at pov_left
    a "Eu amo você, amor."

    pause 4.0

    hide heitor
    with dissolve

    pause 3.0

    scene black
    with fade

    $ duck_music()
    show ana home sad at pov_left

    ana_thought "Acho que meu coração nunca sofreu tanto na vida."

    ana_thought "Mas é a nossa vida. Sofremos juntos e vamos continuar juntos, na alegria, na tristeza, em qualquer situação, porque eu amo você e eu amo tudo que construímos juntos."
    ana_thought "Essa história não termina aqui e nunca vai terminar."

    pause 2.0

    $ restore_music()
    $ set_love_cap_stage("post_australia")
    $ career_phase = "virtualisurg_frontend"
    $ current_country_label = "🇦🇺 Austrália"
    $ add_love(8, "promessa no aeroporto")
    $ unlock_achievement("australia_departure")
    if endgame_replay_mode:
        return
    jump post_australia_route
