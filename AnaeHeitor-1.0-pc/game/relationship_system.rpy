# Shared dating-sim systems for the expanded version.

define system_line = Character(None, what_italic=True)
define ana_thought = Character("Ana", color="#f0a7bb", what_italic=True)
define heitor_thought = Character("Heitor", color="#89c7f5", what_italic=True)
define wa_a = Character("Ana - WhatsApp", color="#f0a7bb")
define wa_h = Character("Heitor - WhatsApp", color="#89c7f5")
define wa_note = Character(None, what_italic=True)

default current_pov = "ana"
default heitor_progress = 0
default ana_progress = 30
default progress_max = 100
default heitor_money = 25
default ana_money = 25
default current_day = 1
default time_slot_index = 0
default queued_notifications = []
default notification_sequence = 0
default first_kiss_done = False
default unlocked_locations = ["poli", "bandejao", "heitor_home", "shop", "work"]
default completed_memories = []
default inventory = []

init python:
    import time as pytime

    time_slots = ["manhã", "tarde", "noite", "madrugada"]

    pov_data = {
        "ana": {
            "name": "Ana",
            "label": "POV da Ana",
            "color": "#f0a7bb",
            "dark": "#3b1724",
        },
        "heitor": {
            "name": "Heitor",
            "label": "POV do Heitor",
            "color": "#89c7f5",
            "dark": "#12324b",
        },
    }

    location_data = [
        {
            "id": "poli",
            "name": "Poli",
            "subtitle": "Listas, corredores e decisões discutíveis.",
        },
        {
            "id": "bandejao",
            "name": "Bandejão",
            "subtitle": "Fila, arroz e decisões difíceis.",
        },
        {
            "id": "heitor_home",
            "name": "Casa do Heitor",
            "subtitle": "Código, sofá e uma chance alta de anime.",
        },
        {
            "id": "shop",
            "name": "Presentes",
            "subtitle": "Pequenas compras, grandes efeitos colaterais.",
        },
        {
            "id": "work",
            "name": "Dinheiro",
            "subtitle": "IC, estágio e a opção economicamente materna.",
        },
    ]

    gift_data = [
        {
            "id": "handmade_note",
            "name": "Bilhete escrito no desespero",
            "cost": 0,
            "love": 4,
            "line": "Custo zero, vulnerabilidade altíssima.",
        },
        {
            "id": "chocolate",
            "name": "Chocolate da Cacau Show",
            "cost": 18,
            "love": 6,
            "line": "O clássico. Funciona porque funciona.",
        },
        {
            "id": "snack",
            "name": "Lanchinho antes da aula",
            "cost": 12,
            "love": 4,
            "line": "Pequeno, barato e emocionalmente estratégico.",
        },
        {
            "id": "earrings",
            "name": "Brincos bonitinhos",
            "cost": 45,
            "love": 10,
            "line": "Perigoso. Pode render um sorriso enorme.",
        },
        {
            "id": "sushi_date",
            "name": "Jantar de sushi",
            "cost": 70,
            "love": 13,
            "line": "Investimento alto. Retorno emocional excelente.",
        },
    ]

    def pov_name():
        return pov_data.get(current_pov, pov_data["ana"])["name"]

    def pov_label():
        return pov_data.get(current_pov, pov_data["ana"])["label"]

    def pov_color(who=None):
        key = who or current_pov
        return pov_data.get(key, pov_data["ana"])["color"]

    def pov_dark(who=None):
        key = who or current_pov
        return pov_data.get(key, pov_data["ana"])["dark"]

    def other_pov(person=None):
        key = person or current_pov
        if key == "ana":
            return "heitor"
        return "ana"

    def time_slot():
        return time_slots[time_slot_index % len(time_slots)]

    def progress_for(person=None):
        key = person or current_pov
        if key == "ana":
            return ana_progress
        return heitor_progress

    def current_progress():
        return progress_for(current_pov)

    def set_progress_for(person, value):
        global heitor_progress, ana_progress
        value = max(0, min(progress_max, value))
        if person == "ana":
            ana_progress = value
        else:
            heitor_progress = value

    def progress_label(value=None, person=None):
        score = progress_for(person) if value is None else value
        if score < 10:
            return "Curiosidade"
        if score < 25:
            return "Atenção"
        if score < 45:
            return "Interesse"
        if score < 65:
            return "Carinho"
        if score < 80:
            return "Paixão"
        return "Amor"

    def queue_notification(message, duration=3.25):
        global notification_sequence
        notification_sequence += 1
        queued_notifications.append((notification_sequence, message, pytime.time() + duration))
        if len(queued_notifications) > 5:
            del queued_notifications[:-5]
        renpy.show_screen("notification_stack")
        renpy.restart_interaction()

    def prune_notifications():
        before = len(queued_notifications)
        now = pytime.time()
        queued_notifications[:] = [toast for toast in queued_notifications if toast[2] > now]
        if before != len(queued_notifications):
            if queued_notifications:
                renpy.restart_interaction()
            else:
                renpy.hide_screen("notification_stack")

    def add_love(amount, reason=None, person=None):
        key = person or current_pov
        set_progress_for(key, progress_for(key) + amount)
        if amount and reason:
            queue_notification("{color=%s}+%d %s para %s: %s{/color}" % (pov_color(key), amount, progress_label(person=key), pov_data[key]["name"], reason))

    def add_partner_love(amount, reason=None):
        add_love(amount, reason, person=other_pov())

    def advance_dialog_section(reason=None):
        add_love(2, reason or "conversa")

    def money_for(person=None):
        key = person or current_pov
        if key == "ana":
            return ana_money
        return heitor_money

    def current_money():
        return money_for(current_pov)

    def format_money(value):
        return ("R$ %.2f" % float(value)).replace(".", ",")

    def current_money_text():
        return format_money(current_money())

    def set_money_for(person, value):
        global heitor_money, ana_money
        value = max(0, value)
        if person == "ana":
            ana_money = value
        else:
            heitor_money = value

    def add_money(amount, reason=None, person=None):
        key = person or current_pov
        set_money_for(key, money_for(key) + amount)
        if amount and reason:
            queue_notification("+%s para %s: %s" % (format_money(amount), pov_data[key]["name"], reason))

    def spend_money(amount, reason=None, person=None):
        key = person or current_pov
        if money_for(key) < amount:
            queue_notification("Dinheiro insuficiente para %s." % pov_data[key]["name"])
            return False
        set_money_for(key, money_for(key) - amount)
        if reason:
            queue_notification("-%s de %s: %s" % (format_money(amount), pov_data[key]["name"], reason))
        return True

    def advance_time(blocks=1):
        global current_day, time_slot_index
        for _i in range(blocks):
            time_slot_index += 1
            if time_slot_index >= len(time_slots):
                time_slot_index = 0
                current_day += 1

    def gift_by_id(gift_id):
        for gift in gift_data:
            if gift["id"] == gift_id:
                return gift
        return None

    def complete_memory(memory_id, love=0, money_reward=0):
        if memory_id in completed_memories:
            return False
        completed_memories.append(memory_id)
        if love:
            add_love(love, "memória desbloqueada")
        if money_reward:
            add_money(money_reward, "memória desbloqueada")
        return True

screen relationship_hud():
    zorder 80

    frame:
        xalign 0.5
        ypos 16
        xsize 1040
        background Solid("#101827dd")
        padding (24, 14)

        hbox:
            spacing 20
            yalign 0.5

            text "[pov_name()]" color pov_color() size 24 xminimum 90 layout "nobreak"
            text "Dia [current_day] - [time_slot()]" color "#f6f7fb" size 24 layout "nobreak"

            hbox:
                spacing 10
                yalign 0.5
                text "[progress_label()]" color pov_color() size 20 xminimum 110 layout "nobreak"
                bar value StaticValue(current_progress(), progress_max) xsize 240 ysize 14 left_bar Solid(pov_color()) right_bar Solid(pov_dark())
                text "[current_progress()]/[progress_max]" color "#f6f7fb" size 18 layout "nobreak"

            text "[current_money_text()]" color "#f6f7fb" size 22 layout "nobreak"

screen notification_stack():
    zorder 130

    timer 0.20 repeat True action Function(prune_notifications)

    if queued_notifications:
        vbox:
            xalign 0.98
            ypos 92
            xmaximum 760
            spacing 8

            for toast in queued_notifications:
                frame at stacked_notify_appear:
                    xalign 1.0
                    background Solid("#101827ee")
                    padding (18, 10)

                    text toast[1]:
                        color "#f6f7fb"
                        size 22
                        text_align 1.0
                        xalign 1.0

screen pov_card(who, title=""):
    zorder 120
    modal True

    key "dismiss" action Return(True)
    key "game_menu" action Return(True)

    add Solid(pov_dark(who))

    button:
        xfill True
        yfill True
        background None
        hover_background None
        action Return(True)

    frame at pov_card_pop:
        xalign 0.5
        yalign 0.5
        xsize 880
        background Solid("#ffffff18")
        padding (46, 38)

        vbox:
            spacing 14
            xalign 0.5

            text pov_data.get(who, pov_data["ana"])["label"]:
                xalign 0.5
                color pov_color(who)
                size 56

            if title:
                text title:
                    xalign 0.5
                    text_align 0.5
                    color "#ffffff"
                    size 30

            text _("Clique para continuar."):
                xalign 0.5
                color "#ffffffcc"
                size 24

transform pov_card_pop:
    alpha 0.0
    yoffset 32
    ease 0.25 alpha 1.0 yoffset 0

transform stacked_notify_appear:
    alpha 0.0
    xoffset 24
    linear 0.15 alpha 1.0 xoffset 0

transform pov_left:
    xpos 0.28
    xanchor 0.5
    yalign 1.0
    zoom 1.08

transform other_right:
    xpos 0.74
    xanchor 0.5
    yalign 1.0
    zoom 0.92

screen gate_notice(title, needed, hint, target_name=""):
    modal True
    zorder 110

    add Solid("#070b13dd")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 980
        background Solid("#182033")
        padding (42, 36)

        vbox:
            spacing 18
            text title color "#ffffff" size 42 xalign 0.5 text_align 0.5
            text hint color "#dfe7f3" size 28 xalign 0.5 text_align 0.5
            if target_name:
                text _("Love necessário com [target_name]: [needed]") color "#f0a7bb" size 26 xalign 0.5
            else:
                text _("Love necessário: [needed]") color "#f0a7bb" size 26 xalign 0.5
            textbutton _("Abrir turno livre") action Return(True) xalign 0.5

screen location_picker(stage):
    modal True
    zorder 100

    add Solid("#090d16ee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1240
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 22

            text _("Turno livre") color "#ffffff" size 46 xalign 0.5
            text _("Escolha uma ação antes da próxima memória.") color "#cfd7e6" size 26 xalign 0.5

            grid 2 3:
                spacing 18
                xalign 0.5

                for loc in location_data:
                    if loc["id"] in unlocked_locations:
                        button:
                            xsize 540
                            ysize 132
                            background Solid("#232d42")
                            hover_background Solid("#33405d")
                            action Return(loc["id"])

                            vbox:
                                spacing 8
                                xalign 0.5
                                yalign 0.5
                                text loc["name"] color "#ffffff" size 32 xalign 0.5

                button:
                    xsize 540
                    ysize 132
                    background Solid("#3b1724")
                    hover_background Solid("#522033")
                    action Return("continue")

                    vbox:
                        spacing 8
                        xalign 0.5
                        yalign 0.5
                        text _("Continuar história") color "#ffffff" size 32 xalign 0.5
                        text _("Tentar avançar para o próximo evento.") color "#f7d7e2" size 20 xalign 0.5 text_align 0.5

screen gift_shop_screen():
    modal True
    zorder 100

    add Solid("#090d16ee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 18

            text _("Presentes") color "#ffffff" size 46 xalign 0.5
            text _("Saldo de [pov_name()]: [current_money_text()]") color "#cfd7e6" size 26 xalign 0.5

            for gift in gift_data:
                button:
                    xfill True
                    yminimum 84
                    background Solid("#232d42")
                    hover_background Solid("#33405d")
                    action Return(gift["id"])

                    hbox:
                        spacing 20
                        yalign 0.5
                        text gift["name"] color "#ffffff" size 26 xminimum 390
                        text format_money(gift["cost"]) color "#f0a7bb" size 24 xminimum 95
                        text "+%d love" % gift["love"] color "#89c7f5" size 24 xminimum 135
                        text gift["line"] color "#cbd5e1" size 20

            textbutton _("Voltar") action Return("back") xalign 0.5

label change_pov(who, title=""):
    $ current_pov = who
    window hide
    call screen pov_card(who, title)
    window show
    return

label relationship_gate(gate_name, needed, hint):
    $ gate_person = other_pov()
    $ gate_person_name = pov_data[gate_person]["name"]

    if progress_for(gate_person) < needed:
        call screen gate_notice(_("Memória bloqueada"), needed, hint, gate_person_name)

    while progress_for(gate_person) < needed:
        $ missing_love = needed - progress_for(gate_person)
        system_line "Ainda faltam [missing_love] pontos de love com [gate_person_name] para esta memória fazer sentido."
        call free_time_phase(gate_name)

    return

label free_time_phase(stage="campus"):
    $ keep_looping = True

    while keep_looping:
        call screen location_picker(stage)
        $ selected_location = _return

        if selected_location == "continue":
            $ keep_looping = False
        elif selected_location == "poli":
            call poli_interaction(stage)
        elif selected_location == "bandejao":
            call bandejao_interaction(stage)
        elif selected_location == "heitor_home":
            call heitor_home_interaction(stage)
        elif selected_location == "shop":
            call gift_phase(stage)
        elif selected_location == "work":
            call money_phase(stage)

    return

label poli_interaction(stage="campus"):
    scene bg desktop_code
    with fade

    if current_pov == "heitor":
        show heitor focused at pov_left
        show ana college thinking at other_right
    else:
        show ana college thinking at pov_left
        show heitor focused at other_right

    menu:
        "Resolver uma lista juntos":
            a "Se a gente dividir por questão, talvez dê tempo."
            h "Ou a gente descobre que a questão 4 depende da 7, que depende de uma epifania."
            show ana college annoyed
            a "Não brinca com esse tipo de coisa."
            $ add_partner_love(4, "lista em dupla")
            $ advance_time()

        "Fazer debug do EP":
            call minigame_debug_ep

        "Reclamar da graduação":
            show ana college happy
            a "Reclamar junto deixa tudo um pouco menos pior."
            show heitor college amused
            h "Na Poli isso quase conta como atividade complementar."
            $ add_partner_love(3, "reclamação acadêmica")
            $ advance_time()

    return

label bandejao_interaction(stage="campus"):
    scene bg bandejao
    with fade

    if current_pov == "heitor":
        show heitor college neutral at pov_left
        show ana college happy at other_right
    else:
        show ana college happy at pov_left
        show heitor college neutral at other_right

    menu:
        "Bandejão speedrun":
            call minigame_bandejao

        "Almoço gratuito e conversa boa":
            if first_kiss_done:
                a "O prato é imprevisível, mas pelo menos a companhia é boa."
                h "Meu plano era sentar perto de você mesmo."
                show ana college embarrassed
                a "Ridículo. Funcionou."
            else:
                a "O prato é imprevisível, mas a conversa tá boa."
                h "Então já foi melhor que a média."
                show ana college happy
                a "Tá, isso eu aceito."
            $ add_partner_love(4, "almoço no bandejão")
            $ advance_time()

        "Debater o ranking dos bandejões":
            show ana college annoyed
            a "Se você falar Física de novo eu vou fingir que não ouvi."
            show heitor college amused
            h "Mas é perto e quase não tem fila."
            $ add_partner_love(3, "debate gastronômico duvidoso")
            $ advance_time()

    return

label heitor_home_interaction(stage="home"):
    scene bg ap_heitor_day
    with fade

    if current_pov == "heitor":
        show heitor home soft_smile at pov_left
        show ana college neutral at other_right
    else:
        show ana college neutral at pov_left
        show heitor home soft_smile at other_right

    menu:
        "Assistir algo no sofá":
            a "Hoje eu vou entender a história."
            h "Você disse isso no episódio passado."
            show ana college embarrassed
            a "Hoje eu vou fingir com mais convicção."
            $ add_partner_love(5, "sofá e série")
            $ advance_time()

        "Jogar alguma coisa":
            a "Eu aviso desde já que os controles são contra mim."
            h "Claro. O controle acordou e escolheu violência."
            $ add_partner_love(5, "jogo em dupla")
            $ advance_time()

        "Cozinhar algo barato":
            h "A receita tem três passos."
            a "Então em algum momento vamos errar quatro."
            $ add_partner_love(4, "jantar improvisado")
            $ advance_time()

    return

label gift_phase(stage="shop"):
    call screen gift_shop_screen
    $ gift_id = _return

    if gift_id == "back":
        return

    $ gift = gift_by_id(gift_id)

    if gift is None:
        return

    $ gift_name = gift["name"]
    $ gift_cost = gift["cost"]
    $ gift_love = gift["love"]

    if gift_cost > 0:
        $ bought_gift = spend_money(gift_cost, gift_name)
    else:
        $ bought_gift = True

    if bought_gift:
        $ inventory.append(gift_name)
        $ add_partner_love(gift_love, gift_name)
        $ advance_time()
        system_line "Você entregou: [gift_name]."
    else:
        system_line "A carteira olhou para o preço e pediu análise assintótica."

    return

label money_phase(stage="money"):
    scene bg desktop_code
    with fade

    if current_pov == "heitor":
        show heitor focused at pov_left
        show ana college thinking at other_right
    else:
        show ana college thinking at pov_left
        show heitor focused at other_right

    menu:
        "Trabalhar na IC":
            a "Hoje é dia de produzir ciência."
            h "Ou pelo menos produzir uma planilha convincente."
            $ add_money(32, "bolsa de IC")
            $ advance_time(2)

        "Pegar uma janela de estágio":
            if "btg_shift" not in completed_memories:
                $ completed_btg_shift = complete_memory("btg_shift", money_reward=80)
                if completed_btg_shift:
                    $ add_partner_love(2, "turno no BTG")
                show ana college happy
                a "Turno de verão no BTG concluído."
                call whatsapp_btg_excerpt
                scene bg desktop_code
                with dissolve
                show ana college happy at pov_left
                show heitor focused at other_right
                h "Saldo emocional e financeiro atualizado."
                show ana college annoyed
                a "Não fala assim que parece relatório."
            else:
                a "Esse turno já foi. O mercado financeiro não vai financiar todos os encontros."
                $ add_money(22, "freela acadêmico")
            $ advance_time(2)

        "Pedir ajuda para a mãe da Ana":
            call mother_money_phase

    return

label mother_money_phase:
    if current_pov == "ana":
        scene bg bedroom_night
        with fade

        show ana home embarrassed at pov_left

        a "Mãe..."
        a "Hipoteticamente, se uma pessoa precisasse investir na própria felicidade..."
        system_line "A mãe da Ana ouviu 'hipoteticamente' e já entendeu a planilha inteira."
        $ add_money(55, "mãe da Ana")
        $ add_partner_love(1, "logística familiar")
        $ advance_time()
    else:
        scene bg desktop_code
        with fade

        show heitor thoughtful at pov_left
        heitor_thought "Pedir dinheiro para a mãe da Ana parece uma permissão que eu definitivamente não tenho."
        $ advance_time()

    return

label minigame_bandejao:
    system_line "Escolha uma estratégia para sobreviver ao bandejão."

    menu:
        "Fila menor":
            show heitor college amused
            h "Física. Perto, rápido e menos fila."
            show ana college annoyed
            a "O arroz tá duro. Tipo, muito duro."
            if current_pov == "ana":
                $ add_love(6, "Física sem fila", person="heitor")
            else:
                system_line "Ana registrou que eficiência e almoço bom continuam sendo métricas diferentes."

        "Prato mais gostoso":
            show ana college super_happy
            a "Central. Arroz soltinho, feijão decente e uma chance real de comida gostosa."
            show heitor college serious
            h "Uma hora de fila para três cubos de estrogonofe. A gente devia ter ido na Física."
            if current_pov == "heitor":
                $ add_love(6, "Central bem escolhida", person="ana")
            else:
                system_line "Heitor aceitou a comida boa, mas a fila ficou aberta em uma aba mental."

        "Sobremesa mais gostosa":
            show ana college happy
            a "Se a sobremesa for boa, eu perdoo muita coisa."
            show heitor college amused
            h "De fato, não posso negar."
            $ add_love(2, "sobremesa estratégica", person="ana")
            $ add_love(2, "sobremesa estratégica", person="heitor")

    $ advance_time()
    return

label minigame_debug_ep:
    $ score = 0

    system_line "Debug emocional do EP. Ache os bugs antes da madrugada."

    menu:
        "Quando o código não compila, você primeiro..."

        "Culpa o compilador.":
            $ score += 0

        "Lê a mensagem de erro.":
            $ score += 2

        "Manda figurinha e espera melhorar.":
            $ score += 1

    menu:
        "Quando a Ana diz que não fez nada no trabalho..."

        "Concorda imediatamente.":
            $ score += 0

        "Mostra a parte que ela entendeu.":
            $ score += 2

        "Muda de assunto para sushi.":
            $ score += 1

    if score >= 3:
        show heitor gentle
        h "Debug feito. Sem julgamento, com paciência."
        show ana college soft
        a "Esse é o melhor tipo."
        $ add_partner_love(7, "debug sem pânico")
    else:
        show ana college thinking
        a "Não resolveu tudo, mas pelo menos a gente tentou junto."
        $ add_partner_love(3, "debug caótico")

    $ advance_time()
    return
