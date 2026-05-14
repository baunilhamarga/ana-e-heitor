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
default ana_money = 200
default current_day = 1
default time_slot_index = 0
default queued_notifications = []
default notification_sequence = 0
default first_kiss_done = False
default current_love_cap_stage = "intro"
default last_code_bug_puzzle = -1
default career_phase = "btg"
default unlocked_locations = ["poli", "bandejao", "heitor_home", "shop", "work"]
default completed_memories = []
default inventory = []
default mother_money_day = 0
default mother_money_requests_today = 0

init python:
    import time as pytime
    import random as py_random
    import re as py_re

    time_slots = ["Manhã", "Tarde", "Noite", "Madrugada"]

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
            "name": "Ganhar dinheiro",
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

    love_cap_data = {
        "intro": {"heitor": 8, "ana": 40},
        "primeiro_contato": {"heitor": 16, "ana": 42},
        "mensagens_iniciais": {"heitor": 22, "ana": 50},
        "ep_yoshi": {"heitor": 24, "ana": 54},
        "primeiro_beijo": {"heitor": 28, "ana": 56},
        "pedido_namoro": {"heitor": 42, "ana": 68},
        "primeiro_eu_te_amo": {"heitor": 60, "ana": 80},
        "australia": {"heitor": 82, "ana": 92},
        "post_australia": {"heitor": 88, "ana": 94},
        "distancia_australia": {"heitor": 92, "ana": 96},
        "france_departure": {"heitor": 100, "ana": 100},
        "birthday_finale": {"heitor": 100, "ana": 100},
    }

    # Relative to the first exported WhatsApp message: 2023-10-24 == day 1.
    story_day_targets = {
        "primeiro_contato": 1,        # 2023-10-24, first WhatsApp day.
        "mensagens_iniciais": 54,    # 2023-12-16, Picles/hamburgueria cluster.
        "primeiro_beijo": 140,       # 2024-03-11, chat recalls the kiss and the fallen phone.
        "pedido_namoro": 154,        # Two weeks after the first kiss in the script.
        "primeiro_eu_te_amo": 164,   # 2024-04-04, first recurring "te amo" cluster.
        "australia": 266,            # 2024-07-15, airport/Australia departure window.
        "post_australia": 266,
        "distancia_australia": 714,  # 2025-10-06, France/double-degree arrival window.
        "france_departure": 714,
    }

    story_time_slot_targets = {
        "primeiro_contato": 3,
        "mensagens_iniciais": 2,
        "primeiro_beijo": 1,
        "pedido_namoro": 2,
        "primeiro_eu_te_amo": 3,
        "australia": 2,
        "post_australia": 2,
        "distancia_australia": 2,
        "france_departure": 2,
    }

    free_time_start_targets = {
        "primeiro_contato": (1, 1),      # Day 1 afternoon, right after the first Bandejão talk.
        "mensagens_iniciais": (2, 0),    # Day 2 morning, after the madrugada X-ray chat.
        "primeiro_beijo": (55, 0),        # After the Yoshi EP cluster, before the next Bandejão.
    }

    free_time_action_caps = {
        "primeiro_contato": (1, 2),      # Free actions can reach Day 1 night, but the memory is dawn.
    }

    free_time_continue_requirements = {
        "mensagens_iniciais": {
            "love": 14,
            "person": "heitor",
            "money": 25,
        },
        "distancia_australia": {
            "love": 90,
            "person": "heitor",
        },
    }

    career_data = {
        "btg": {
            "memory": "btg_shift",
            "money": 80,
            "repeat_money": 22,
            "love": 2,
            "title": "Summer job no BTG concluído.",
            "reason": "plantão corporativo sobrevivido",
            "repeat_reason": "bico acadêmico honestíssimo",
        },
        "virtualisurg_frontend": {
            "memory": "virtualisurg_frontend_shift",
            "money": 95,
            "repeat_money": 35,
            "love": 3,
            "title": "Sprint de front-end na VirtualiSurg concluída.",
            "reason": "div centralizada com sucesso",
            "repeat_reason": "ajuste de interface remunerado",
        },
        "virtualisurg_xr": {
            "memory": "virtualisurg_xr_shift",
            "money": 115,
            "repeat_money": 45,
            "love": 3,
            "title": "Entrega de XR na VirtualiSurg concluída.",
            "reason": "bug em realidade estendida",
            "repeat_reason": "protótipo de XR sem tontura",
        },
    }

    code_bug_puzzles = [
        {
            "title": "Ache o bug.",
            "answer": 5,
            "success": "Boa. Esse <= tentava ler uma posição que não existe.",
            "failure": "Quase. O problema era o limite do 'for' passando do tamanho do vetor.",
            "lines": [
                "{color=#c084fc}#include{/color} {color=#f0f6fc}<stdio.h>{/color}",
                "{color=#89c7f5}int{/color} main({color=#89c7f5}void{/color}) {{",
                "    {color=#89c7f5}int{/color} notas[[5] = {{ {color=#f8d66d}8{/color}, {color=#f8d66d}7{/color}, {color=#f8d66d}9{/color}, {color=#f8d66d}6{/color}, {color=#f8d66d}10{/color} }};",
                "    {color=#89c7f5}int{/color} soma = {color=#f8d66d}0{/color};",
                "    {color=#ff7b72}for{/color} ({color=#89c7f5}int{/color} i = {color=#f8d66d}0{/color}; i <= {color=#f8d66d}5{/color}; i++) {{",
                "        soma += notas[[i];",
                "    }",
                "    printf({color=#a5d6ff}\"%d\\\\n\"{/color}, soma);",
                "}",
            ],
        },
        {
            "title": "Ache o bug.",
            "answer": 5,
            "success": "Isso. Um igual só muda o valor; dois iguais comparam.",
            "failure": "Quase. A linha perigosa era o if usando = em vez de ==.",
            "lines": [
                "{color=#c084fc}#include{/color} {color=#f0f6fc}<stdio.h>{/color}",
                "{color=#89c7f5}int{/color} main({color=#89c7f5}void{/color}) {{",
                "    {color=#89c7f5}int{/color} senha = {color=#f8d66d}0{/color};",
                "    {color=#ff7b72}scanf{/color}({color=#a5d6ff}\"%d\"{/color}, &senha);",
                "    {color=#ff7b72}if{/color} (senha = {color=#f8d66d}220324{/color}) {{",
                "        printf({color=#a5d6ff}\"entrou\\\\n\"{/color});",
                "    }",
                "    {color=#ff7b72}return{/color} {color=#f8d66d}0{/color};",
                "}",
            ],
        },
        {
            "title": "Ache o bug.",
            "answer": 4,
            "success": "Exato. Esse ponto e vírgula encerra o if cedo demais.",
            "failure": "Quase. O bug era o ponto e vírgula logo depois do if.",
            "lines": [
                "{color=#c084fc}#include{/color} {color=#f0f6fc}<stdio.h>{/color}",
                "{color=#89c7f5}int{/color} main({color=#89c7f5}void{/color}) {{",
                "    {color=#89c7f5}int{/color} fome = {color=#f8d66d}1{/color};",
                "    {color=#ff7b72}if{/color} (fome == {color=#f8d66d}1{/color}); {{",
                "        printf({color=#a5d6ff}\"bandejao\\\\n\"{/color});",
                "    }",
                "    {color=#ff7b72}return{/color} {color=#f8d66d}0{/color};",
                "}",
            ],
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

    def pov_button_color(who=None):
        key = who or current_pov
        if key == "ana":
            return "#6a2d45"
        return "#1f4e72"

    def other_pov(person=None):
        key = person or current_pov
        if key == "ana":
            return "heitor"
        return "ana"

    def time_slot():
        return time_slots[time_slot_index % len(time_slots)]

    def time_slot_icon():
        icons = {
            "Manhã": "☀️",
            "Tarde": "🌤️",
            "Noite": "🌙",
            "Madrugada": "🌌",
        }
        return icons.get(time_slot(), "🕒")

    def bandejao_is_open():
        return time_slot() not in ("Noite", "Madrugada")

    def free_action_tint():
        slot = time_slot()
        if slot == "Manhã":
            return "#fff1b822"
        if slot == "Tarde":
            return "#ffb15f24"
        if slot == "Noite":
            return "#07132f72"
        return "#05071688"

    def free_turn_overlay():
        slot = time_slot()
        if slot == "Manhã":
            return "#fff2bd4f"
        if slot == "Tarde":
            return "#ff9f2a66"
        if slot == "Noite":
            return "#071a3aa8"
        return "#030816dd"

    def free_turn_room_filter():
        slot = time_slot()
        if slot == "Manhã":
            return "#fff4c72f"
        if slot == "Tarde":
            return "#ff9b2f3c"
        if slot == "Noite":
            return "#06163358"
        return "#03081670"

    def heitor_home_background():
        if time_slot() in ("Noite", "Madrugada"):
            return "bg ap_heitor_night"
        return "bg ap_heitor_day"

    def bedroom_background():
        if time_slot() in ("Manhã", "Tarde"):
            return "bg ap_heitor_day"
        return "bg bedroom_night"

    def free_turn_background():
        if time_slot() == "Manhã":
            return "bg ap_heitor_day"
        if time_slot() == "Tarde":
            return "bg ap_heitor_day"
        if time_slot() == "Noite":
            return "bg ap_heitor_night"
        return "bg bedroom_night"

    def show_free_turn_scene():
        renpy.scene()
        renpy.show(free_turn_background())
        renpy.show("free_turn_room_filter", what=Solid(free_turn_room_filter()))

    def show_free_action_scene(bg_name):
        renpy.scene()
        renpy.show(bg_name)
        renpy.show("free_time_tint", what=Solid(free_action_tint()))

    def set_love_cap_stage(stage):
        global current_love_cap_stage
        current_love_cap_stage = stage or "intro"

    def love_cap_for(person=None, stage=None):
        key = person or current_pov
        cap_stage = stage or current_love_cap_stage
        caps = love_cap_data.get(cap_stage)
        if caps is None:
            return progress_max
        return caps.get(key, progress_max)

    def pick_code_bug_puzzle():
        global last_code_bug_puzzle
        if len(code_bug_puzzles) <= 1:
            last_code_bug_puzzle = 0
            return code_bug_puzzles[0]

        available_indexes = [i for i in range(len(code_bug_puzzles)) if i != last_code_bug_puzzle]
        index = py_random.SystemRandom().choice(available_indexes)
        last_code_bug_puzzle = index
        return code_bug_puzzles[index]

    def location_available(location_id):
        if current_love_cap_stage == "primeiro_contato" and location_id != "work":
            return False
        if location_id in ("heitor_home", "shop") and not first_kiss_done:
            return False
        if location_id == "bandejao" and not bandejao_is_open():
            return False
        if location_id == "bandejao" and current_money() < 2:
            return False
        return True

    def locked_location_message(location_id):
        if current_love_cap_stage == "primeiro_contato":
            if location_id == "bandejao":
                return "Acabaram de sair do bandejão."
            if location_id == "poli":
                return "Ainda é cedo para chamar para estudar."
            if location_id == "heitor_home":
                return "Ta maluca Ana! Você nem conhece ele direito!"
            if location_id == "shop":
                return "Presentes ficam para depois."
        if location_id == "bandejao" and not bandejao_is_open():
            return "O bandejão está fechado agora."
        if location_id == "bandejao" and current_money() < 2:
            return "Precisa de R$ 2,00 para o bandejão."
        if location_id == "heitor_home" and current_pov == "ana" and not first_kiss_done:
            return "Ta maluca Ana! Você nem conhece ele direito!"
        if location_id == "heitor_home":
            return "Esse rolê ainda não faz sentido."
        if location_id == "shop":
            return "Presentes ficam para depois."
        return "Ainda não disponível."

    def resolved_continue_requirements(stage, needed=0, target_person=None):
        base = dict(free_time_continue_requirements.get(stage, {}))
        if needed:
            base["love"] = needed
            base["person"] = target_person or other_pov()
        return base

    def free_time_can_continue(stage="campus", needed=0, target_person=None):
        requirements = resolved_continue_requirements(stage, needed, target_person)
        love_needed = requirements.get("love", 0)
        money_needed = requirements.get("money", 0)
        love_person = requirements.get("person", target_person or other_pov())

        if love_needed and progress_for(love_person) < love_needed:
            return False
        if money_needed and current_money() < money_needed:
            return False
        return True

    def possessive_name(person):
        if person == "ana":
            return "da Ana"
        return "do Heitor"

    def free_time_continue_hint(stage="campus", needed=0, target_person=None):
        requirements = resolved_continue_requirements(stage, needed, target_person)
        parts = []
        all_met = True

        love_needed = requirements.get("love", 0)
        if love_needed:
            target = requirements.get("person", target_person or other_pov())
            current = progress_for(target)
            label = progress_label(person=target)
            owner = possessive_name(target)
            if current >= love_needed:
                parts.append("%s %s: %d" % (label, owner, love_needed))
            else:
                all_met = False
                parts.append("%s %s: %d/%d" % (label, owner, current, love_needed))

        money_needed = requirements.get("money", 0)
        if money_needed:
            current_cash = current_money()
            if current_cash >= money_needed:
                parts.append("saldo: %s" % format_money(money_needed))
            else:
                all_met = False
                parts.append("saldo: %s/%s, falta %s" % (format_money(current_cash), format_money(money_needed), format_money(money_needed - current_cash)))

        if not parts:
            return "Requisito: nenhum."

        if all_met:
            return "Requisito cumprido - " + " | ".join(parts)

        return "Requisito - " + " | ".join(parts)

    def story_day_target(stage):
        return story_day_targets.get(stage)

    def continue_will_pass_time(stage):
        target_block = story_time_block_target(stage)
        return target_block is not None and current_time_block() < target_block

    def advance_to_story_day(stage):
        target_block = story_time_block_target(stage)
        if target_block is None or current_time_block() >= target_block:
            return 0

        before = current_time_block()
        set_time_block(target_block)
        return target_block - before

    def time_tuple_to_block(time_tuple):
        if time_tuple is None:
            return None
        day, slot = time_tuple
        return (day - 1) * len(time_slots) + slot

    def apply_free_time_start(stage):
        start_block = time_tuple_to_block(free_time_start_targets.get(stage))
        if start_block is not None and current_time_block() < start_block:
            set_time_block(start_block)

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

    def capped_progress_text(label):
        feminine_labels = ("Curiosidade", "Atenção", "Paixão")
        masculine_labels = ("Interesse", "Carinho", "Amor")
        if label in feminine_labels:
            return "%s máxima atingida, por agora..." % label
        if label in masculine_labels:
            return "%s máximo atingido, por agora..." % label
        return "%s no limite, por agora..." % label

    def popup_reason(reason):
        reasons = {
            "bolsa de IC": "IC pagou.",
            "bandejão": "Bandejão pago.",
            "hamburgueria": "Hamburgueria paga.",
            "lanche improvisado": "Lanche pago. O plano B também alimenta.",
            "memória desbloqueada": "Memória desbloqueada.",
            "lista em dupla": "Lista em dupla.",
            "reclamação acadêmica": "Reclamar também aproxima.",
            "almoço no bandejão": "Companhia boa salva o prato.",
            "debate duvidoso": "Ranking de bandejão.",
            "sofá e série": "Sofá e série. Entender o plot é opcional.",
            "jogo em dupla": "Jogo em dupla.",
            "jantar improvisado": "Jantar improvisado. Tecnicamente comestível.",
            "debug sem pânico": "Debug sem pânico. Amor também tem breakpoint.",
            "debug caótico": "Debug caótico.",
            "EP salvo na madrugada": "EP salvo na madrugada. Yoshi não venceu hoje.",
            "mensagens iniciais": "Mensagem vai, mensagem vem.",
            "oi estrategicamente simples": "Um oi simples. Risco baixo, coração alto.",
            "histórico do WhatsApp mapeado": "Histórico mapeado. Dataset emocional carregado.",
            "bom dia transcontinental": "Bom dia atravessou o fuso.",
            "boa noite transcontinental": "Boa noite atravessou o fuso.",
            "redundância afetiva": "Bom dia e boa noite.",
            "três meses de distância": "Três meses longe. Saudade.",
            "França e duplo diploma": "França e duplo diploma.",
            "promessa no aeroporto": "Promessa no aeroporto. Coração em modo embarque.",
            "calistenia": "Calistenia também é legal.",
            "desenhar": "Desenho também conta como charme.",
            "bandejão da Física": "Física???????",
            "bandejão Central": "Central bem defendido. Ana aprova.",
            "bandejão da Química": "Química ficou no meio termo, como sempre.",
            "hamburgueria mais tranquila": "Hamburgueria tranquila.",
            "volta no parque": "Volta no parque. Paz também é date.",
            "primeiro beijo": "Primeiro beijo. O ônibus quase atrapalhou.",
            "pedido de namoro": "Pedido de namoro. Finalmente oficial.",
            "primeiro eu te amo": "Primeiro eu te amo.",
            "Física sem fila": "Física sem fila. Heitor chama isso de vitória.",
            "Central bem escolhida": "Central escolhido. Ana chama isso de bom senso.",
            "sobremesa estratégica": "Decisão impecável.",
            "percebeu o que ela entendeu": "Ele percebeu o que ela entendeu. Ponto para a paciência.",
            "pausa para sushi": "Pausa para sushi. Sempre existe argumento melhor.",
            "Aline salvou o dia": "Aline salva o dia.",
            "plantão corporativo sobrevivido": "BTG.",
            "bico acadêmico honestíssimo": "Bico acadêmico.",
            "div centralizada com sucesso": "Div centralizada.",
            "ajuste de interface remunerado": "Pixel também paga boleto.",
            "bug em realidade estendida": "XR entregue.",
            "protótipo de XR sem tontura": "Protótipo de XR.",
        }
        if not reason:
            return ""
        return reasons.get(reason, str(reason).replace("_", " "))

    def notification_duration(message):
        plain = py_re.sub(r"\{[^}]+\}", "", message)
        return min(9.0, max(4.75, 3.25 + (len(plain) / 28.0)))

    def queue_notification(message, duration=None):
        global notification_sequence
        if duration is None:
            duration = notification_duration(message)
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
        cap = love_cap_for(key)
        current = progress_for(key)
        available = max(0, cap - current)
        applied = min(amount, available)

        if applied > 0:
            set_progress_for(key, current + applied)
            if reason:
                queue_notification("{color=%s}+%d %s para %s: %s{/color}" % (pov_color(key), applied, progress_label(person=key), pov_data[key]["name"], popup_reason(reason)))
        elif amount and reason:
            queue_notification("{color=%s}%s{/color}" % (pov_color(key), capped_progress_text(progress_label(person=key))))

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
            queue_notification("💰 +%s para %s: %s" % (format_money(amount), pov_data[key]["name"], popup_reason(reason)))

    def spend_money(amount, reason=None, person=None):
        key = person or current_pov
        if money_for(key) < amount:
            queue_notification("💸 Dinheiro insuficiente para %s." % pov_data[key]["name"])
            return False
        set_money_for(key, money_for(key) - amount)
        if reason:
            queue_notification("💸 -%s de %s: %s" % (format_money(amount), pov_data[key]["name"], popup_reason(reason)))
        return True

    def advance_time(blocks=1):
        global current_day, time_slot_index
        for _i in range(blocks):
            if time_slot_index < 2:
                time_slot_index += 1
            else:
                time_slot_index = 0
                current_day += 1

    def current_time_block():
        return (current_day - 1) * len(time_slots) + time_slot_index

    def set_time_block(block_index):
        global current_day, time_slot_index
        block_index = max(0, block_index)
        current_day = (block_index // len(time_slots)) + 1
        time_slot_index = block_index % len(time_slots)

    def story_time_block_target(stage):
        target_day = story_day_target(stage)
        if target_day is None:
            return None
        target_slot = story_time_slot_targets.get(stage, time_slot_index)
        return (target_day - 1) * len(time_slots) + target_slot

    def next_gameplay_time_block(block_index):
        slot = block_index % len(time_slots)
        if slot < 2:
            return block_index + 1
        if slot == 2:
            return block_index + 2
        return block_index + 1

    def free_time_action_cap_block(stage):
        cap_block = time_tuple_to_block(free_time_action_caps.get(stage))
        if cap_block is not None:
            return cap_block
        return story_time_block_target(stage)

    def advance_free_time(stage, blocks=1):
        target_block = free_time_action_cap_block(stage)
        if target_block is None:
            advance_time(blocks)
            return blocks

        before = current_time_block()
        after = before
        for _i in range(blocks):
            next_block = next_gameplay_time_block(after)
            if next_block > target_block:
                after = target_block
                break
            after = next_block
        if after > before:
            set_time_block(after)
        return max(0, after - before)

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
        background Solid("#101827dd")
        padding (22, 12)

        hbox:
            spacing 18
            yalign 0.5

            text "[pov_name()]" color pov_color() size 24 layout "nobreak"
            text "📅 Dia [current_day]" color "#f6f7fb" size 24 layout "nobreak"
            text "[time_slot_icon()] [time_slot()]" color "#f6f7fb" size 24 layout "nobreak"

            hbox:
                spacing 10
                yalign 0.5
                text "[progress_label()]" color pov_color() size 20 xminimum 108 layout "nobreak" yalign 0.5
                bar value StaticValue(current_progress(), progress_max) xsize 220 ysize 14 left_bar Solid(pov_color()) right_bar Solid(pov_dark()) yalign 0.5
                text "[current_progress()]/[progress_max]" color "#f6f7fb" size 18 layout "nobreak" yalign 0.5

            text "💵 [current_money_text()]" color "#f6f7fb" size 22 layout "nobreak"

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
                text _("Love necessário de [target_name]: [needed]") color "#f0a7bb" size 26 xalign 0.5
            else:
                text _("Love necessário: [needed]") color "#f0a7bb" size 26 xalign 0.5
            textbutton _("Abrir turno livre") action Return(True) xalign 0.5

screen location_picker(stage, needed=0, target_person=None):
    modal True
    zorder 70

    default continue_ready = free_time_can_continue(stage, needed, target_person)
    default locked_location_id = None
    default locked_location_hint = ""

    add Solid(free_turn_overlay())

    frame:
        xalign 0.5
        yalign 0.5
        background Solid(pov_dark())
        padding (34, 30)

        vbox:
            spacing 22

            text _("Turno livre") color pov_color() size 46 xalign 0.5
            text _("Escolha uma ação antes da próxima memória.") color "#cfd7e6" size 26 xalign 0.5

            grid 2 3:
                spacing 18
                xalign 0.5

                for loc in location_data:
                    if loc["id"] in unlocked_locations:
                        $ loc_id = loc["id"]
                        $ loc_ready = location_available(loc["id"])
                        $ bandejao_closed = loc_id == "bandejao" and not bandejao_is_open()
                        button:
                            xsize 540
                            ysize 132
                            background Solid("#232d42" if loc_ready else "#202532")
                            hover_background Solid("#33405d" if loc_ready else "#2b3140")
                            action If(loc_ready, Return(loc_id), [SetScreenVariable("locked_location_id", loc_id), SetScreenVariable("locked_location_hint", locked_location_message(loc_id))])

                            vbox:
                                spacing 7
                                xalign 0.5
                                yalign 0.5
                                text loc["name"] color ("#ffffff" if loc_ready else "#7f8797") size 32 xalign 0.5
                                if loc_id == "bandejao":
                                    if bandejao_closed:
                                        text _("O bandejão está fechado agora.") color "#a2a9b8" size 20 xalign 0.5
                                    else:
                                        text _("Gasta R$ 2,00") color ("#f7d7e2" if loc_ready else "#a2a9b8") size 20 xalign 0.5
                                if (not loc_ready) and (not bandejao_closed) and locked_location_id == loc_id and locked_location_hint:
                                    text locked_location_hint color "#f7d7e2" size 18 xalign 0.5 text_align 0.5

                button:
                    xsize 540
                    ysize 132
                    background Solid(pov_button_color() if continue_ready else "#242936")
                    hover_background Solid(pov_color() if continue_ready else "#242936")
                    sensitive continue_ready
                    action Return("continue")

                    vbox:
                        spacing 8
                        xalign 0.5
                        yalign 0.5
                        text _("Continuar história") color ("#ffffff" if continue_ready else "#7f8797") size 32 xalign 0.5
                        if stage != "primeiro_contato":
                            text free_time_continue_hint(stage, needed, target_person) color ("#f7d7e2" if continue_ready else "#a2a9b8") size 20 xalign 0.5 text_align 0.5
                            if continue_ready and continue_will_pass_time(stage):
                                text _("Isso passará o tempo.") color "#cfd7e6" size 18 xalign 0.5 text_align 0.5

screen code_bug_screen(puzzle):
    modal True
    zorder 115

    default selected_line = None

    add Solid("#080c14ee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        background Solid("#151c2c")
        padding (32, 28)

        vbox:
            spacing 20

            text puzzle["title"] color "#ffffff" size 40 xalign 0.5 text_align 0.5
            text _("Clique na linha com o bug e confirme.") color "#cfd7e6" size 24 xalign 0.5

            frame:
                xfill True
                background Solid("#0d1117")
                padding (14, 12)

                vbox:
                    spacing 2

                    for line_number, code_line in enumerate(puzzle["lines"], 1):
                        button:
                            xfill True
                            yminimum 38
                            background Solid("#1f6feb55" if selected_line == line_number else "#0d1117")
                            hover_background Solid("#1f6feb33")
                            action SetScreenVariable("selected_line", line_number)

                            hbox:
                                spacing 16
                                yalign 0.5
                                text "%02d" % line_number color "#6e7681" size 22 xsize 44 text_align 1.0
                                text code_line color "#c9d1d9" size 24

            hbox:
                xalign 0.5
                spacing 16

                textbutton _("Confirmar"):
                    sensitive selected_line is not None
                    action Return(selected_line)

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

label quick_change_pov(who):
    $ current_pov = who
    show expression Solid(pov_color(who) + "cc") as quick_pov_flash onlayer overlay
    with Dissolve(0.15)
    pause 0.1
    hide quick_pov_flash onlayer overlay
    with Dissolve(0.10)
    return

label relationship_gate(gate_name, needed, hint):
    $ set_love_cap_stage(gate_name)
    $ gate_person = other_pov()
    $ gate_person_name = pov_data[gate_person]["name"]

    if progress_for(gate_person) < needed:
        call screen gate_notice(_("Memória bloqueada"), needed, hint, gate_person_name)

    while progress_for(gate_person) < needed:
        $ missing_love = needed - progress_for(gate_person)
        system_line "Ainda faltam [missing_love] pontos de love de [gate_person_name] para esta memória fazer sentido."
        call free_time_phase(gate_name, needed, gate_person)

    return

label free_time_phase(stage="campus", needed=0, target_person=None):
    $ set_love_cap_stage(stage)
    $ apply_free_time_start(stage)
    $ keep_looping = True

    while keep_looping:
        window hide
        $ show_free_turn_scene()
        call screen location_picker(stage, needed, target_person)
        window auto
        $ selected_location = _return

        if selected_location == "continue":
            $ advance_to_story_day(stage)
            $ keep_looping = False
        elif selected_location == "poli":
            call poli_interaction(stage)
        elif selected_location == "bandejao":
            $ paid_bandejao = spend_money(2, "bandejão")
            if paid_bandejao:
                call bandejao_interaction(stage)
        elif selected_location == "heitor_home":
            call heitor_home_interaction(stage)
        elif selected_location == "shop":
            call gift_phase(stage)
        elif selected_location == "work":
            if stage == "primeiro_contato":
                call mother_money_phase(stage)
            else:
                call money_phase(stage)

    return

label poli_interaction(stage="campus"):
    $ show_free_action_scene("bg desktop_code")
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
            h "Ou a gente descobre que a questão 20 depende da 19, que depende da 18, que depende da 17, que depende da 16..."
            show ana college annoyed
            a "N-Não brinca com esse tipo de coisa!!!"
            $ add_partner_love(4, "lista em dupla")
            $ advance_free_time(stage)

        "Fazer debug do EP":
            call minigame_debug_ep(stage)

        "Reclamar da graduação":
            system_line "A Ana fica 20 minutos reclamando de como ela não leva jeito pra computação."
            show ana college happy
            a "Reclamar deixa tudo um pouco menos pior."
            show heitor college amused
            h "Na Poli isso quase conta como atividade complementar."
            $ add_partner_love(3, "reclamação acadêmica")
            $ advance_free_time(stage)

    return

label bandejao_interaction(stage="campus"):
    $ show_free_action_scene("bg bandejao")
    with fade

    if current_pov == "heitor":
        show heitor college neutral at pov_left
        show ana college happy at other_right
    else:
        show ana college happy at pov_left
        show heitor college neutral at other_right

    menu:
        "Bandejão speedrun":
            call minigame_bandejao(stage)

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
            $ advance_free_time(stage)

        "Debater o ranking dos bandejões":
            show ana college annoyed
            a "Se você falar Física de novo eu vou fingir que não ouvi."
            show heitor college amused
            h "Mas é perto e quase não tem fila."
            $ add_partner_love(3, "debate duvidoso")
            $ advance_free_time(stage)

    return

label heitor_home_interaction(stage="home"):
    $ show_free_action_scene(heitor_home_background())
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
            $ advance_free_time(stage)

        "Jogar alguma coisa":
            a "Eu aviso desde já que os controles são contra mim."
            h "Claro. O controle acordou e escolheu violência."
            $ add_partner_love(5, "jogo em dupla")
            $ advance_free_time(stage)

        "Cozinhar algo barato":
            h "A receita tem três passos."
            a "Então em algum momento vamos errar quatro."
            $ add_partner_love(4, "jantar improvisado")
            $ advance_free_time(stage)

    return

label gift_phase(stage="shop"):
    $ show_free_action_scene("bg desktop_code")
    with fade

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
        $ advance_free_time(stage)
        system_line "Você entregou: [gift_name]."
    else:
        system_line "A carteira olhou para o preço e pediu análise assintótica."

    return

label money_phase(stage="money"):
    $ show_free_action_scene("bg desktop_code")
    with fade

    if current_pov == "heitor":
        show heitor focused at pov_left
        show ana college thinking at other_right
    else:
        show ana college thinking at pov_left
        show heitor focused at other_right

    menu:
        "Trabalhar na IC":
            if current_pov == "ana":
                a "Eu não fiz quase nada e eles elogiam o que eu fiz como se fosse a melhor coisa do mundo."
                h "Meu Deus, 2h de reunião! Vocês tão pesquisando mesmo ou batendo papo?"
            else:
                h "Mais uma noite sem dormir, é hoje que eu termino esse paper."
            $ add_money(32, "bolsa de IC")
            $ advance_free_time(stage, 2)

        "Pegar uma janela de estágio" if current_pov == "ana":
            call ana_internship_phase(stage)

        "Pedir ajuda para a nanãe" if current_pov == "ana":
            call mother_money_phase(stage)

    return

label ana_internship_phase(stage="money"):
    $ job = career_data.get(career_phase, career_data["btg"])
    $ job_title = job["title"]

    $ add_money(job["money"], job["reason"])
    $ add_partner_love(job["love"], job["reason"])
    show ana college happy
    a "[job_title]"
    if career_phase == "btg":
        call whatsapp_btg_excerpt
        $ show_free_action_scene("bg desktop_code")
        with dissolve
        show ana college happy at pov_left
        show heitor focused at other_right
    elif career_phase == "virtualisurg_frontend":
        h "Nossa, como eu amo front-end, quero trabalhar com isso pro resto da vida."
        show ana college happy
        a "Finalmente centralizei a div, que dia produtivo."
    else:
        h "XR na VirtualiSurg. Agora o bug pode estar no código ou no espaço."
        show ana college sad
        a "Que saudade do front..."
    h "Dinheiro a gente faz..."
    show ana college annoyed
    a "Até parece"

    $ advance_free_time(stage, 2)
    return

label mother_money_phase(stage="money"):
    if current_pov == "ana":
        $ mother_money_day_changed = mother_money_day != current_day
        if mother_money_day_changed:
            $ mother_money_day = current_day
            $ mother_money_requests_today = 0
        $ mother_money_requests_today += 1

        $ show_free_action_scene(bedroom_background())
        with fade

        show ana home embarrassed at pov_left

        a "Nanãe..."
        a "Manda dinheiro pro iFoods, por favor?"

        if mother_money_requests_today >= 3:
            system_line "Aline: Que isso Ana, ta passando fome?"
            system_line "Dessa vez o pix não veio. Talvez seja melhor esperar amanhã."
        else:
            $ add_money(200, "Aline salvou o dia")
            system_line "Não demora muito para o pix cair."
        
        $ advance_free_time(stage)
    else:
        $ show_free_action_scene("bg desktop_code")
        with fade

        show heitor thoughtful at pov_left
        heitor_thought "Pedir dinheiro para a mãe da Ana parece uma permissão que eu definitivamente não tenho."
        $ advance_free_time(stage)

    return

label minigame_bandejao(stage="campus"):
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
            h "Sabe muito."
            $ add_love(2, "sobremesa estratégica", person="ana")
            $ add_love(2, "sobremesa estratégica", person="heitor")

    $ advance_free_time(stage)
    return

label minigame_debug_ep(stage="campus"):
    $ score = 0

    system_line "Debug emocional do EP. Ache os bugs antes da madrugada."

    $ code_puzzle = pick_code_bug_puzzle()
    call screen code_bug_screen(code_puzzle)
    $ selected_code_line = _return

    if selected_code_line == code_puzzle["answer"]:
        $ score += 2
        $ code_result_text = code_puzzle["success"]
    else:
        $ code_result_text = code_puzzle["failure"]

    system_line "[code_result_text]"

    if current_pov == "heitor":
        menu:
            "Quando a Ana diz que não fez nada no trabalho..."

            "Concorda imediatamente.":
                system_line "Ana não pareceu muito convencida."

            "Mostra a parte que ela entendeu.":
                show heitor gentle
                h "Você entendeu essa parte aqui. O resto a gente ajeita."
                show ana college soft
                a "Tá... isso ajuda."
                $ add_love(4, "percebeu o que ela entendeu", person="ana")

            "Muda de assunto para sushi.":
                show heitor college amused
                h "Pausa tática: sushi?"
                show ana college happy
                a "Agora sim você falou algo que eu entendo."
                $ add_love(2, "pausa para sushi", person="ana")

    if score >= 2:
        show heitor gentle
        h "Debug feito. Com paciência."
        show ana college soft
        a "Esse é o melhor jeito."
        $ add_partner_love(7, "debug sem pânico")
    else:
        show ana college thinking
        a "Não resolveu tudo, mas pelo menos a gente tentou junto."
        $ add_partner_love(3, "debug caótico")

    $ advance_free_time(stage)
    return
