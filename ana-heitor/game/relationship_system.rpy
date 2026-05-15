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
default special_day_label = ""
default current_country_label = "🇧🇷 Brasil"
default endgame_mode = False
default endgame_replay_mode = False
default queued_notifications = []
default notification_sequence = 0
default first_kiss_done = False
default dating_started = False
default date_gate_notice_seen = False
default current_love_cap_stage = "intro"
default last_code_bug_puzzle = -1
default career_phase = "btg"
default unlocked_locations = ["poli", "bandejao", "heitor_home", "shop", "work"]
default completed_memories = []
default inventory = []
default purchased_gifts = []
default photo_gift_completed = False
default photo_gift_completion_count = 0
default mother_money_day = 0
default mother_money_requests_today = 0
default rhythm_play_count = 0
default rhythm_prop_unlock = False
default rhythm_state = {}
default rhythm_unlocked_song_index = 0
default rhythm_unlocked_difficulties = {}
default rhythm_best_results = {}
default rhythm_locked_song_clicks = {}
default rhythm_locked_difficulty_clicks = {}

init python:
    import time as pytime
    import random as py_random
    import re as py_re

    rhythm_lanes = [
        {"id": "left", "key": "←", "x": 150},
        {"id": "down", "key": "↓", "x": 300},
        {"id": "up", "key": "↑", "x": 450},
        {"id": "right", "key": "→", "x": 600},
    ]

    rhythm_arrow_crops = {
        "left": (982, 38, 150, 150),
        "down": (1850, 150, 156, 156),
        "up": (1850, 2, 156, 156),
        "right": (1210, 40, 150, 150),
    }

    rhythm_receptor_crops = {
        "left": (310, 238, 150, 150),
        "down": (2, 236, 150, 150),
        "up": (788, 236, 150, 150),
        "right": (158, 238, 150, 150),
    }

    rhythm_hit_crops = {
        "left": (1430, 35, 150, 150),
        "down": (38, 42, 157, 153),
        "up": (515, 39, 155, 148),
        "right": (1665, 35, 150, 150),
    }

    rhythm_song_order = ["din_don_dan", "butterfly", "kiss", "propaganda", "batom_e_cereja", "sosseguei"]

    rhythm_tracks = {
        "din_don_dan": {
            "title": "Din Don Dan",
            "artist": "Ryu☆ feat. Mayumi Morinaga",
            "music": "ddr/din_don_dan.ogg",
            "sm": "ddr/din_don_dan.sm",
            "duration": 108.008,
        },
        "butterfly": {
            "title": "Butterfly",
            "artist": "SMiLE.dk",
            "music": "ddr/butterfly.ogg",
            "sm": "ddr/butterfly.sm",
            "duration": 93.989,
        },
        "kiss": {
            "title": "I Was Made For Lovin' You",
            "artist": "Kiss",
            "music": "ddr/kiss.mp3",
            "sm": "ddr/kiss.sm",
            "duration": 238.263,
        },
        "propaganda": {
            "title": "Propaganda",
            "artist": "Jorge & Mateus",
            "music": "ddr/propaganda.mp3",
            "sm": "ddr/propaganda.sm",
            "duration": 139.442,
        },
        "batom_e_cereja": {
            "title": "Batom de Cereja",
            "artist": "Israel & Rodolffo",
            "music": "ddr/batom_e_cereja.mp3",
            "sm": "ddr/batom_e_cereja.sm",
            "duration": 177.502,
        },
        "sosseguei": {
            "title": "Sosseguei",
            "artist": "Jorge & Mateus",
            "music": "ddr/sosseguei.mp3",
            "sm": "ddr/sosseguei.sm",
            "duration": 197.695,
        },
    }

    bgm_tracks = {
        "heitor_default": "audio/pwaa/13. Initial Investigation 2001.mp3",
        "ana_default": "audio/pwaa/14. Maya Fey - Turnabout Sisters 2001.mp3",
        "daily_light": "audio/pwaa/19. Simple Folk.mp3",
        "date_fun": "audio/pwaa/19. Simple Folk.mp3",
        "game_fun": "audio/pwaa/31. The Blue Badger - I Want to Protect You.mp3",
        "study_debug": "audio/pwaa/05. Tricks and Deductions.mp3",
        "work_money": "audio/pwaa/06. Phoenix Wright - Objection! 2001.mp3",
        "choice_tension": "audio/pwaa/04. Cross-Examination - Moderato 2001.mp3",
        "playful_push": "audio/pwaa/07. Cross-Examination - Allegro 2001.mp3",
        "funny_win": "audio/pwaa/25. Victory! - Our First Win.mp3",
        "romance_soft": "audio/pwaa/27. The Ballad of Turnabout Sisters.mp3",
        "ana_sad": "audio/pwaa/17. Reminiscences - Maya's Sorrow.mp3",
        "distance_sad": "audio/pwaa/22. Reminiscences - The DL-6 Incident.mp3",
        "airport_tension": "audio/pwaa/10. Suspense.mp3",
        "big_transition": "audio/pwaa/26. Phoenix Wright_ Ace Attorney - Ending.mp3",
        "birthday": "audio/pwaa/27. The Ballad of Turnabout Sisters.mp3",
        "endgame": "audio/pwaa/30. Ema Skye - Turnabout Sisters 2005.mp3",
    }

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
            "emoji": "📚",
            "subtitle": "Listas, corredores e decisões discutíveis.",
        },
        {
            "id": "bandejao",
            "name": "Bandejão",
            "emoji": "🍽️",
            "subtitle": "Fila, arroz e decisões difíceis.",
        },
        {
            "id": "heitor_home",
            "name": "Rolê em casa",
            "emoji": "🏠",
            "subtitle": "Código, sofá e uma chance alta de anime.",
        },
        {
            "id": "shop",
            "name": "Presentes",
            "emoji": "🎁",
            "subtitle": "Pequenas compras, grandes efeitos colaterais.",
        },
        {
            "id": "work",
            "name": "Fazer dinheiro",
            "emoji": "💵",
            "subtitle": "IC, estágio e a opção economicamente materna.",
        },
    ]

    gift_data = [
        {
            "id": "handmade_note",
            "name": "Bilhete escrito no desespero",
            "emoji": "📝",
            "cost": 0,
            "love": 4,
            "line": "Custo zero, vulnerabilidade altíssima.",
        },
        {
            "id": "chocolate",
            "name": "Chocolate da Cacau Show",
            "emoji": "🍫",
            "cost": 30,
            "love": 6,
            "line": "O clássico. Funciona porque funciona.",
        },
        {
            "id": "snack",
            "name": "Lanchinho antes da aula",
            "emoji": "🥪",
            "cost": 12,
            "love": 4,
            "line": "Pequeno e barato.",
        },
        {
            "id": "earrings",
            "name": "Brincos bonitinhos",
            "emoji": "💎",
            "cost": 300,
            "love": 10,
            "line": "Dinheiro a gente faz... Pode render um sorriso enorme.",
        },
        {
            "id": "sushi_date",
            "name": "Jantar de sushi",
            "emoji": "🍣",
            "cost": 99.99,
            "love": 13,
            "line": "Salmãozinho grelhado, sashimi, camarão com catupiry? Humm...",
        },
        {
            "id": "photo_gift",
            "name": "Fazer um presente caprichado com fotos",
            "emoji": "🖼️",
            "cost": 10,
            "love": 24,
            "line": "Tesoura emocional, fotos e capricho de verdade.",
        },
    ]

    photo_gift_difficulties = {
        "facil": {
            "name": "Fácil",
            "size": 3,
            "reward": 14,
            "moves": 28,
        },
        "medio": {
            "name": "Médio",
            "size": 4,
            "reward": 18,
            "moves": 52,
        },
        "dificil": {
            "name": "Difícil",
            "size": 5,
            "reward": 24,
            "moves": 85,
        },
    }

    love_cap_data = {
        "intro": {"heitor": 8, "ana": 40},
        "primeiro_contato": {"heitor": 16, "ana": 42},
        "mensagens_iniciais": {"heitor": 22, "ana": 50},
        "ep_yoshi": {"heitor": 24, "ana": 54},
        "primeiro_beijo": {"heitor": 28, "ana": 56},
        "pedido_namoro": {"heitor": 55, "ana": 68},
        "primeiro_eu_te_amo": {"heitor": 70, "ana": 80},
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
        "australia": 549,            # Around 13 months after the dating start event.
        "post_australia": 639,       # Roughly 3 months after the Australia departure.
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
        },
        "distancia_australia": {
            "love": 90,
            "person": "heitor",
        },
        "pedido_namoro": {
            "gifts": ["chocolate", "earrings"],
        },
    }

    free_time_blocked_hints = {
        "mensagens_iniciais": "Antes da próxima memória, falta se aproximar um pouco mais do Heitor. Tentem se conhecer melhor.",
        "primeiro_beijo": "Antes da próxima memória, ainda falta a coragem certa para aquele momento fazer sentido. Tentem criar mais clima.",
        "pedido_namoro": "Depois do primeiro beijo, ainda precisa caber um pouco de rotina: mensagens, encontros baratos e coragem acumulada.",
        "distancia_australia": "Antes da próxima memória, a distância precisa virar rotina: mensagens e paciência",
    }

    endgame_memory_data = [
        {"name": "Introdução - Bandejão", "label": "endgame_intro_replay"},
        {"name": "Raio-x e primeiras mensagens", "label": "mensagem_raiox"},
        {"name": "Picles", "label": "picles"},
        {"name": "EP do Yoshi", "label": "ep_yoshi"},
        {"name": "Primeiro beijo", "label": "primeiro_beijo"},
        {"name": "Pedido de namoro", "label": "pedido_namoro"},
        {"name": "Primeiro eu te amo", "label": "primeiro_eu_te_amo"},
        {"name": "Um ano feliz", "label": "ano_feliz"},
        {"name": "Austrália", "label": "despedida_aeroporto"},
        {"name": "Distância da Austrália", "label": "australia_distance_arc"},
        {"name": "França", "label": "france_departure_arc"},
        {"name": "Feliz aniversário", "label": "birthday_finale"},
    ]

    endgame_state_data = [
        {
            "name": "🇧🇷 Brasil - Ana",
            "pov": "ana",
            "stage": "primeiro_eu_te_amo",
            "country": "🇧🇷 Brasil",
            "career": "btg",
        },
        {
            "name": "🇧🇷 Brasil - Heitor",
            "pov": "heitor",
            "stage": "primeiro_eu_te_amo",
            "country": "🇧🇷 Brasil",
            "career": "btg",
        },
        {
            "name": "🇦🇺 Austrália - Ana com saudade",
            "pov": "ana",
            "stage": "distancia_australia",
            "country": "🇧🇷 Brasil",
            "career": "virtualisurg_frontend",
        },
        {
            "name": "🇦🇺 Austrália - Heitor",
            "pov": "heitor",
            "stage": "distancia_australia",
            "country": "🇦🇺 Austrália",
            "career": "virtualisurg_frontend",
        },
        {
            "name": "🇫🇷 França - Ana",
            "pov": "ana",
            "stage": "france_departure",
            "country": "🇧🇷 Brasil",
            "career": "virtualisurg_xr",
        },
        {
            "name": "🇫🇷 França - Heitor",
            "pov": "heitor",
            "stage": "france_departure",
            "country": "🇫🇷 França",
            "career": "virtualisurg_xr",
        },
    ]

    achievement_data = [
        {
            "id": "first_kiss",
            "name": "Primeiro beijo",
            "description": "Chegou ao ponto de ônibus que mudou tudo.",
        },
        {
            "id": "dating_started",
            "name": "Agora é oficial",
            "description": "Aceitou o pedido de namoro.",
        },
        {
            "id": "first_love",
            "name": "Eu te amo",
            "description": "Chegou ao primeiro eu te amo.",
        },
        {
            "id": "australia_departure",
            "name": "Fuso horário desbloqueado",
            "description": "Passou pela despedida da Austrália.",
        },
        {
            "id": "birthday_complete",
            "name": "História concluída",
            "description": "Viu o presente de aniversário até o final.",
        },
        {
            "id": "earrings_bought",
            "name": "Dinheiro a gente faz",
            "description": "Comprou os brincos do pedido.",
        },
        {
            "id": "aline_limit",
            "name": "Tá passando fome?",
            "description": "Pediu dinheiro para a nanãe vezes demais no mesmo dia.",
        },
        {
            "id": "photo_gift",
            "name": "Capricho com fotos",
            "description": "Fez um presente com mosaico de fotos.",
        },
        {
            "id": "photo_gift_hard",
            "name": "Capricho máximo",
            "description": "Completou o mosaico difícil.",
        },
        {
            "id": "photo_gift_five",
            "name": "Fotogênica",
            "description": "Completou 5 mosaicos de foto.",
        },
        {
            "id": "photo_no_skip",
            "name": "Artista",
            "description": "Completou um mosaico sem pular.",
        },
        {
            "id": "daily_sushi",
            "name": "Grelhado ou sashimi?",
            "description": "Visitou o Sushi no Dia a dia.",
        },
        {
            "id": "propaganda_seen",
            "name": "Propaganda desbloqueada",
            "description": "Jogou Jorge e Mateus no minigame de ritmo.",
        },
        {
            "id": "all_rhythm_songs",
            "name": "DJ da relação",
            "description": "Desbloqueou todas as músicas do minigame de ritmo.",
        },
        {
            "id": "ddr_master",
            "name": "DDR Master",
            "description": "Tentou jogar uma música na sua dificuldade mais difícil.",
        },
        {
            "id": "rhythm_perfect",
            "name": "Perfeccionista",
            "description": "Atingiu pontuação perfeita em qualquer música.",
        },
        {
            "id": "heitor_money_10000",
            "name": "Falei que dinheiro a gente faz",
            "description": "Acumulou R$ 10.000,00 no POV do Heitor.",
        },
        {
            "id": "full_love_both",
            "name": "Tim amo<>Também",
            "description": "Atingiu 100 de Amor com Ana e Heitor.",
        },
        {
            "id": "endgame_mode",
            "name": "Pós-jogo infinito",
            "description": "Entrou no modo Dia a dia infinito.",
        },
        {
            "id": "endgame_memory_replay",
            "name": "Como é que foi mesmo?",
            "description": "Reviveu uma memória no modo Pós-jogo.",
        },
    ]

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
            "repeat_reason": "XR sem tontura",
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

    def bgm_for_pov():
        if current_pov == "ana":
            return "ana_default"
        return "heitor_default"

    def play_bgm(track_id=None, fadein=1.2, fadeout=1.2):
        track = bgm_tracks.get(track_id or bgm_for_pov())
        if not track:
            return
        renpy.music.play(track, channel="music", loop=True, fadein=fadein, fadeout=fadeout, if_changed=True)

    def stop_bgm(fadeout=1.2):
        renpy.music.stop(channel="music", fadeout=fadeout)

    def set_music_volume(volume, delay=0.8):
        renpy.music.set_volume(volume, delay=delay, channel="music")

    def duck_music(delay=0.8):
        set_music_volume(0.38, delay)

    def restore_music(delay=0.8):
        set_music_volume(1.0, delay)

    def time_slot():
        normalize_time_state()
        return time_slots[time_slot_index % len(time_slots)]

    def time_slot_icon():
        icons = {
            "Manhã": "☀️",
            "Tarde": "🌤️",
            "Noite": "🌙",
            "Madrugada": "🌌",
        }
        return icons.get(time_slot(), "🕒")

    def day_status_text():
        if special_day_label:
            return special_day_label
        return "📅 Dia %d" % current_day

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
        gift_needed = requirements.get("gifts", [])
        love_person = requirements.get("person", target_person or other_pov())

        if love_needed and progress_for(love_person) < love_needed:
            return False
        if money_needed and current_money() < money_needed:
            return False
        if gift_needed and not all(gift_id in purchased_gifts for gift_id in gift_needed):
            return False
        return True

    def free_time_has_continue_requirements(stage="campus", needed=0, target_person=None):
        requirements = resolved_continue_requirements(stage, needed, target_person)
        return bool(requirements.get("love", 0) or requirements.get("money", 0) or requirements.get("gifts", []))

    def free_time_blocked_hint(stage="campus", custom_hint=None):
        if custom_hint:
            return custom_hint
        return free_time_blocked_hints.get(stage, "Antes da próxima memória, falta cumprir alguns requisitos no dia a dia.")

    def ana_distance_day(stage):
        return current_pov == "ana" and stage == "distancia_australia"

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

        gift_needed = requirements.get("gifts", [])
        for gift_id in gift_needed:
            gift = gift_by_id(gift_id)
            gift_name = gift["name"] if gift else gift_id
            if gift_id in purchased_gifts:
                parts.append("%s comprado" % gift_name)
            else:
                all_met = False
                parts.append("comprar %s" % gift_name)

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
        if score < 24:
            return "Atenção"
        if score < 42:
            return "Interesse"
        if score < 62:
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
            "jantar barato": "Jantar barato pago.",
            "Tavares no iFood": "Tavares pago. Barato, honesto e polêmico.",
            "memória desbloqueada": "Memória desbloqueada.",
            "lista em dupla": "Lista em dupla.",
            "reclamação acadêmica": "Reclamar também aproxima.",
            "almoço no bandejão": "Companhia boa salva o prato.",
            "debate duvidoso": "Ranking de bandejão.",
            "sofá e série": "Sofá e série. Entender o plot é opcional.",
            "jogo em dupla": "Jogo em dupla.",
            "jogo de habilidade": "Jogo de habilidade. Setas sobreviveram.",
            "jogo de história": "Jogo de história. Cinema com botão.",
            "jogo de aventura": "Jogo de aventura. Cooperação sob pressão.",
            "jantar improvisado": "Jantar improvisado.",
            "parmegiana do Tavares": "Tavares: Heitor defende, Ana tolera.",
            "plantão no Crossing": "Crossing. Pesquisa também paga.",
            "debug sem pânico": "Debug sem pânico. Amor também tem breakpoint.",
            "debug caótico": "Debug caótico.",
            "EP salvo na madrugada": "EP salvo na madrugada. Yoshi não venceu hoje.",
            "mensagens iniciais": "Mensagem vai, mensagem vem.",
            "oi estrategicamente simples": "Um oi simples. Risco baixo, coração alto.",
            "histórico do WhatsApp mapeado": "Histórico mapead.",
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

    def ensure_achievement_store():
        if not hasattr(persistent, "achievements") or persistent.achievements is None:
            persistent.achievements = {}
        return persistent.achievements

    def achievement_by_id(achievement_id):
        for achievement in achievement_data:
            if achievement["id"] == achievement_id:
                return achievement
        return None

    def achievement_unlocked(achievement_id):
        return bool(ensure_achievement_store().get(achievement_id))

    def unlock_achievement(achievement_id):
        store = ensure_achievement_store()
        if store.get(achievement_id):
            return False
        achievement = achievement_by_id(achievement_id)
        if achievement is None:
            return False
        store[achievement_id] = True
        renpy.save_persistent()
        queue_notification("{color=#f5c84b}🏆 Conquista desbloqueada: %s{/color}" % achievement["name"], duration=7.5)
        return True

    def unlocked_achievement_count():
        store = ensure_achievement_store()
        return sum(1 for achievement in achievement_data if store.get(achievement["id"]))

    def confirm_message_pt(message):
        translations = {
            "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.": "Tem certeza que quer voltar ao menu principal?\nO progresso não salvo será perdido.",
            "Are you sure you want to quit?": "Tem certeza que quer sair?",
            "Are you sure you want to overwrite your save?": "Tem certeza que quer sobrescrever este save?",
            "Are you sure you want to load this save?": "Tem certeza que quer carregar este save?",
            "Are you sure you want to delete this save?": "Tem certeza que quer apagar este save?",
            "Are you sure you want to end the replay?": "Tem certeza que quer encerrar o replay?",
            "Are you sure you want to begin skipping?": "Tem certeza que quer começar a pular?",
            "Are you sure you want to skip to the next choice?": "Tem certeza que quer pular até a próxima escolha?",
            "Are you sure you want to skip unseen dialogue to the next choice?": "Tem certeza que quer pular diálogos não vistos até a próxima escolha?",
        }
        return translations.get(message, message)

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
            if heitor_progress >= 100 and ana_progress >= 100:
                unlock_achievement("full_love_both")
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
        if key == "heitor" and money_for(key) >= 10000:
            unlock_achievement("heitor_money_10000")
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
        normalize_time_state()
        for _i in range(blocks):
            if time_slot_index < 2:
                time_slot_index += 1
            else:
                time_slot_index = 0
                current_day += 1

    def normalize_time_state():
        global current_day, time_slot_index
        current_day = max(1, int(current_day))
        time_slot_index = int(time_slot_index) % len(time_slots)

    def current_time_block():
        normalize_time_state()
        return (current_day - 1) * len(time_slots) + time_slot_index

    def set_time_block(block_index):
        global current_day, time_slot_index
        block_index = max(0, block_index)
        current_day = (block_index // len(time_slots)) + 1
        time_slot_index = block_index % len(time_slots)
        normalize_time_state()

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
        target_block = story_time_block_target(stage)
        if target_block is not None and target_block % len(time_slots) == 3:
            return target_block - 1
        return target_block

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

    def gift_is_visible(gift):
        if gift["id"] == "photo_gift" and not dating_started:
            return False
        if gift["id"] == "earrings" and (current_pov == "ana" or gift["id"] in purchased_gifts):
            return False
        return True

    def gift_is_available(gift):
        if not gift_is_visible(gift):
            return False
        if gift["id"] == "snack" and time_slot() == "Noite":
            return False
        return current_money() >= gift["cost"]

    def gift_status_text(gift):
        if gift["id"] == "earrings" and gift["id"] in purchased_gifts:
            return "Já comprado para o pedido."
        if gift["id"] == "sushi_date" and ana_distance_day(current_love_cap_stage):
            return "Sushi sozinha. Bom, mas com uma cadeira sobrando."
        if gift["id"] == "snack" and time_slot() == "Noite":
            return "Lanchinho antes da aula não combina com noite."
        if current_money() < gift["cost"]:
            return "Saldo insuficiente."
        return gift["line"]

    def gift_photo_files():
        return sorted([
            path for path in renpy.list_files()
            if path.startswith("images/gift_photos/")
            and path.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ])

    def pick_gift_photo():
        photos = gift_photo_files()
        if not photos:
            return None
        return py_random.SystemRandom().choice(photos)

    def puzzle_adjacent(index, blank, size):
        row, col = divmod(index, size)
        blank_row, blank_col = divmod(blank, size)
        return abs(row - blank_row) + abs(col - blank_col) == 1

    def shuffled_photo_puzzle(size, moves):
        pieces = list(range(size * size))
        blank = len(pieces) - 1
        rng = py_random.SystemRandom()
        previous_blank = None
        for _i in range(moves):
            candidates = [i for i in range(len(pieces)) if puzzle_adjacent(i, blank, size) and i != previous_blank]
            if not candidates:
                candidates = [i for i in range(len(pieces)) if puzzle_adjacent(i, blank, size)]
            index = rng.choice(candidates)
            pieces[blank], pieces[index] = pieces[index], pieces[blank]
            previous_blank, blank = blank, index
        if pieces == list(range(size * size)):
            pieces[blank], pieces[blank - 1] = pieces[blank - 1], pieces[blank]
        return pieces

    def puzzle_move(pieces, index, size):
        new_pieces = list(pieces)
        blank = new_pieces.index(len(new_pieces) - 1)
        if puzzle_adjacent(index, blank, size):
            new_pieces[blank], new_pieces[index] = new_pieces[index], new_pieces[blank]
        return new_pieces

    def puzzle_move_in_place(pieces, index, size):
        blank = pieces.index(len(pieces) - 1)
        if puzzle_adjacent(index, blank, size):
            pieces[blank], pieces[index] = pieces[index], pieces[blank]
        return None

    def puzzle_solved(pieces):
        return pieces == list(range(len(pieces)))

    def photo_puzzle_layout(photo, size):
        source_w, source_h = renpy.image_size(photo)
        max_w, max_h = 820, 620
        scale = min(float(max_w) / source_w, float(max_h) / source_h, 1.0)
        display_w = max(size, int(source_w * scale))
        display_h = max(size, int(source_h * scale))
        tile_w = max(1, display_w // size)
        tile_h = max(1, display_h // size)
        return {
            "scale": scale,
            "width": tile_w * size,
            "height": tile_h * size,
            "tile_width": tile_w,
            "tile_height": tile_h,
        }

    def scaled_photo_display(photo, size):
        layout = photo_puzzle_layout(photo, size)
        return im.Crop(im.FactorScale(photo, layout["scale"]), (0, 0, layout["width"], layout["height"]))

    def puzzle_piece_display(photo, piece, size):
        layout = photo_puzzle_layout(photo, size)
        tile_w = layout["tile_width"]
        tile_h = layout["tile_height"]
        row, col = divmod(piece, size)
        return im.Crop(im.FactorScale(photo, layout["scale"]), (col * tile_w, row * tile_h, tile_w, tile_h))

    def photo_puzzle_piece_displays(photo, size):
        layout = photo_puzzle_layout(photo, size)
        tile_w = layout["tile_width"]
        tile_h = layout["tile_height"]
        scaled_photo = im.FactorScale(photo, layout["scale"])
        pieces = []
        for piece in range(size * size):
            row, col = divmod(piece, size)
            pieces.append(im.Crop(scaled_photo, (col * tile_w, row * tile_h, tile_w, tile_h)))
        return pieces

    def read_renpy_text(path):
        data = renpy.file(path).read()
        if isinstance(data, bytes):
            return data.decode("utf-8", "ignore")
        return data

    def sm_tag(content, tag, default=""):
        match = py_re.search(r"#%s:([^;]*);" % tag, content, py_re.I)
        if match:
            return match.group(1).strip()
        return default

    def sm_bpm(content):
        bpms = sm_tag(content, "BPMS", "0=120")
        first = bpms.split(",")[0]
        if "=" in first:
            first = first.split("=", 1)[1]
        try:
            return float(first)
        except Exception:
            return 120.0

    def sm_bpm_segments(content):
        raw_bpms = sm_tag(content, "BPMS", "0=120")
        segments = []
        for item in raw_bpms.split(","):
            if "=" not in item:
                continue
            beat_text, bpm_text = item.split("=", 1)
            try:
                segments.append((float(beat_text.strip()), float(bpm_text.strip())))
            except Exception:
                pass
        if not segments:
            segments = [(0.0, 120.0)]
        return sorted(segments, key=lambda segment: segment[0])

    def sm_beat_to_seconds(beat, bpm_segments):
        total = 0.0
        for index, segment in enumerate(bpm_segments):
            start_beat, bpm = segment
            end_beat = bpm_segments[index + 1][0] if index + 1 < len(bpm_segments) else beat
            if beat <= start_beat:
                break
            covered_beats = min(beat, end_beat) - start_beat
            if covered_beats > 0:
                total += covered_beats * (60.0 / bpm)
            if beat < end_beat:
                break
        return total

    def sm_offset(content):
        try:
            return float(sm_tag(content, "OFFSET", "0"))
        except Exception:
            return 0.0

    def sm_charts(track_id):
        track = rhythm_tracks[track_id]
        content = read_renpy_text(track["sm"])
        charts = []
        for chart_index, block in enumerate(content.split("#NOTES:")[1:]):
            block = block.split(";", 1)[0]
            fields = block.split(":", 5)
            if len(fields) < 6:
                continue
            style = fields[0].strip()
            difficulty = fields[2].strip() or "Edit"
            meter = fields[3].strip() or "?"
            if "dance-single" not in style:
                continue
            charts.append({
                "id": "%s_%02d_%s" % (track_id, chart_index, difficulty.lower().replace(" ", "_")),
                "track_id": track_id,
                "index": chart_index,
                "difficulty": difficulty,
                "meter": meter,
                "notes": fields[5],
            })
        return sorted(charts, key=lambda chart: int(chart["meter"]) if str(chart["meter"]).isdigit() else 99)

    def rhythm_chart_unlocked(track_id, chart):
        unlocked = rhythm_unlocked_difficulties.get(track_id, 0)
        charts = sm_charts(track_id)
        for index, candidate in enumerate(charts):
            if candidate["id"] == chart["id"]:
                return index <= unlocked
        return False

    def rhythm_unlock_next_chart(track_id, chart):
        charts = sm_charts(track_id)
        current_index = 0
        for index, candidate in enumerate(charts):
            if candidate["id"] == chart["id"]:
                current_index = index
                break
        rhythm_unlocked_difficulties[track_id] = max(rhythm_unlocked_difficulties.get(track_id, 0), min(current_index + 1, len(charts) - 1))

    def rhythm_track_unlocked(track_id):
        try:
            return rhythm_song_order.index(track_id) <= rhythm_unlocked_song_index
        except ValueError:
            return False

    def rhythm_unlock_next_song(track_id):
        global rhythm_unlocked_song_index
        try:
            index = rhythm_song_order.index(track_id)
        except ValueError:
            return
        rhythm_unlocked_song_index = max(rhythm_unlocked_song_index, min(index + 1, len(rhythm_song_order) - 1))
        if track_id == "propaganda":
            unlock_achievement("propaganda_seen")
        if rhythm_unlocked_song_index >= len(rhythm_song_order) - 1:
            unlock_achievement("all_rhythm_songs")

    def rhythm_song_entries():
        entries = []
        for index, track_id in enumerate(rhythm_song_order):
            if index <= rhythm_unlocked_song_index:
                entries.append({"track_id": track_id, "locked": False, "message": ""})
            elif index == rhythm_unlocked_song_index + 1:
                previous_id = rhythm_song_order[index - 1]
                entries.append({
                    "track_id": track_id,
                    "locked": True,
                    "message": "🔒 Jogue %s para desbloquear" % rhythm_tracks[previous_id]["title"],
                })
                break
        return entries

    def rhythm_result_tag(accuracy):
        if accuracy >= 98:
            return "💎 Perfect"
        if accuracy >= 85:
            return "🌟 Great"
        if accuracy >= 40:
            return "✅ Pass"
        return "💥 Fail"

    def rhythm_chart_result_text(chart):
        result = rhythm_best_results.get(chart["id"])
        if not result:
            return "🏁 Sem score"
        return "%s  Max %d" % (rhythm_result_tag(result.get("accuracy", 0)), result.get("score", 0))

    def rhythm_record_result(chart):
        current = rhythm_best_results.get(chart["id"], {"score": -1, "accuracy": 0})
        score = rhythm_state.get("score", 0)
        accuracy = rhythm_accuracy()
        if score > current.get("score", -1):
            rhythm_best_results[chart["id"]] = {"score": score, "accuracy": accuracy}

    def rhythm_locked_song_press(track_id):
        global rhythm_unlocked_song_index
        rhythm_locked_song_clicks[track_id] = rhythm_locked_song_clicks.get(track_id, 0) + 1
        if rhythm_locked_song_clicks[track_id] >= 10:
            try:
                index = rhythm_song_order.index(track_id)
            except ValueError:
                return
            rhythm_unlocked_song_index = max(rhythm_unlocked_song_index, index)
            rhythm_locked_song_clicks[track_id] = 0
            queue_notification("Ok, não precisa spammar, pode jogar.")
            renpy.restart_interaction()

    def rhythm_locked_difficulty_press(track_id, chart):
        key = chart["id"]
        rhythm_locked_difficulty_clicks[key] = rhythm_locked_difficulty_clicks.get(key, 0) + 1
        if rhythm_locked_difficulty_clicks[key] >= 10:
            charts = sm_charts(track_id)
            unlock_index = rhythm_unlocked_difficulties.get(track_id, 0)
            for index, candidate in enumerate(charts):
                if candidate["id"] == chart["id"]:
                    unlock_index = index
                    break
            rhythm_unlocked_difficulties[track_id] = max(rhythm_unlocked_difficulties.get(track_id, 0), unlock_index)
            rhythm_locked_difficulty_clicks[key] = 0
            queue_notification("Ok, não precisa spammar, pode jogar.")
            renpy.restart_interaction()

    def sm_chart_notes(track_id, chart):
        content = read_renpy_text(rhythm_tracks[track_id]["sm"])
        max_time = rhythm_tracks[track_id].get("duration", 600.0)
        bpm_segments = sm_bpm_segments(content)
        offset = sm_offset(content)
        notes = []
        measures = [m for m in chart["notes"].replace("\r", "").split(",") if m.strip()]
        for measure_index, measure in enumerate(measures):
            rows = [row.strip() for row in measure.split("\n") if row.strip() and not row.strip().startswith("//")]
            if not rows:
                continue
            for row_index, row in enumerate(rows):
                if len(row) < 4:
                    continue
                note_beat = (measure_index * 4.0) + ((row_index * 4.0) / float(len(rows)))
                note_time = sm_beat_to_seconds(note_beat, bpm_segments) - offset
                if note_time < 0 or note_time > max_time:
                    continue
                for col, char in enumerate(row[:4]):
                    if char in ("1", "2", "4"):
                        notes.append({"time": note_time, "lane": rhythm_lanes[col]["id"], "hit": False, "miss": False})
        return notes

    def start_rhythm_state(track_id, chart):
        global rhythm_state
        notes = sm_chart_notes(track_id, chart)
        rhythm_state = {
            "track_id": track_id,
            "title": rhythm_tracks[track_id]["title"],
            "difficulty": chart["difficulty"],
            "meter": chart["meter"],
            "notes": notes,
            "start": pytime.time() + 1.25,
            "score": 0,
            "combo": 0,
            "max_combo": 0,
            "hits": 0,
            "misses": 0,
            "judgement": "Prepare...",
            "hit_effects": [],
            "done": False,
        }
        return rhythm_state

    def rhythm_now():
        if not rhythm_state:
            return 0.0
        return pytime.time() - rhythm_state.get("start", pytime.time())

    def rhythm_update():
        if not rhythm_state or rhythm_state.get("done"):
            return
        now = rhythm_now()
        for note in rhythm_state["notes"]:
            if not note["hit"] and not note["miss"] and now - note["time"] > 0.28:
                note["miss"] = True
                rhythm_state["misses"] += 1
                rhythm_state["combo"] = 0
                rhythm_state["judgement"] = "Errou"
        notes_finished = rhythm_state["notes"] and all(note["hit"] or note["miss"] for note in rhythm_state["notes"])
        if notes_finished:
            rhythm_state["judgement"] = "Música terminando..."
            if not renpy.music.is_playing(channel="music"):
                rhythm_state["done"] = True

    def rhythm_hit(lane):
        if not rhythm_state or rhythm_state.get("done"):
            return
        now = rhythm_now()
        candidates = [
            note for note in rhythm_state["notes"]
            if note["lane"] == lane and not note["hit"] and not note["miss"] and abs(note["time"] - now) <= 0.28
        ]
        if not candidates:
            rhythm_state["combo"] = 0
            rhythm_state["judgement"] = "Fora do tempo"
            return
        note = min(candidates, key=lambda item: abs(item["time"] - now))
        delta = abs(note["time"] - now)
        note["hit"] = True
        rhythm_state["hit_effects"].append({"lane": lane, "until": now + 0.14})
        rhythm_state["hits"] += 1
        rhythm_state["combo"] += 1
        rhythm_state["max_combo"] = max(rhythm_state["max_combo"], rhythm_state["combo"])
        if delta <= 0.08:
            rhythm_state["score"] += 1000
            rhythm_state["judgement"] = "Perfeito"
        elif delta <= 0.16:
            rhythm_state["score"] += 700
            rhythm_state["judgement"] = "Bom"
        else:
            rhythm_state["score"] += 400
            rhythm_state["judgement"] = "Quase"

    def rhythm_visible_notes():
        now = rhythm_now()
        visible = []
        lane_x = dict((lane["id"], lane["x"]) for lane in rhythm_lanes)
        for note in rhythm_state.get("notes", []):
            if note["hit"] or note["miss"]:
                continue
            delta = note["time"] - now
            if -0.25 <= delta <= 2.0:
                visible.append({
                    "x": lane_x[note["lane"]],
                    "y": 49 + int(delta * 265),
                    "lane": note["lane"],
                })
        return visible

    def rhythm_visible_hit_effects():
        now = rhythm_now()
        effects = []
        lane_x = dict((lane["id"], lane["x"]) for lane in rhythm_lanes)
        kept = []
        for effect in rhythm_state.get("hit_effects", []):
            if effect["until"] >= now:
                kept.append(effect)
                effects.append({
                    "x": lane_x[effect["lane"]],
                    "lane": effect["lane"],
                })
        rhythm_state["hit_effects"] = kept
        return effects

    def rhythm_arrow_display(lane):
        return im.Crop("NOTE_assets.png", rhythm_arrow_crops[lane])

    def rhythm_receptor_display(lane):
        return im.Crop("NOTE_assets.png", rhythm_receptor_crops[lane])

    def rhythm_hit_display(lane):
        return im.Crop("NOTE_assets.png", rhythm_hit_crops[lane])

    def rhythm_accuracy():
        if not rhythm_state:
            return 0
        total = rhythm_state.get("hits", 0) + rhythm_state.get("misses", 0)
        if total <= 0:
            return 0
        return int((rhythm_state["hits"] * 100) / total)

    def rhythm_reward():
        accuracy = rhythm_accuracy()
        if accuracy >= 85:
            return 6
        if accuracy >= 65:
            return 4
        if accuracy >= 40:
            return 2
        return 1

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

            text "[pov_name()]" color pov_color() size 24 layout "nobreak" yalign 0.5
            text "[day_status_text()]" color "#f6f7fb" size 24 layout "nobreak" yalign 0.5
            text "[time_slot_icon()] [time_slot()]" color "#f6f7fb" size 24 layout "nobreak" yalign 0.5

            hbox:
                spacing 10
                yalign 0.5
                text "[progress_label()]" color pov_color() size 20 xminimum 108 layout "nobreak" yalign 0.5
                bar value StaticValue(current_progress(), progress_max) xsize 220 ysize 14 left_bar Solid(pov_color()) right_bar Solid(pov_dark()) yalign 0.5
                text "[current_progress()]/[progress_max]" color "#f6f7fb" size 18 layout "nobreak" yalign 0.5

            text "💵 [current_money_text()]" color "#f6f7fb" size 22 layout "nobreak" yalign 0.5
            text "[current_country_label]" color "#f6f7fb" size 24 layout "nobreak" yalign 0.5
            textbutton "🏆":
                yalign 0.5
                ysize 30
                text_size 22
                text_color "#f5c84b"
                text_hover_color "#ffe08a"
                text_yalign 0.5
                background None
                hover_background Solid("#f5c84b22")
                action Show("achievement_list_screen")

screen notification_stack():
    zorder 130

    timer 0.20 repeat True action Function(prune_notifications)

    if queued_notifications:
        vbox:
            xalign 0.98
            ypos 92
            xmaximum 1840
            spacing 8

            for toast in queued_notifications:
                frame at stacked_notify_appear:
                    xalign 1.0
                    xmaximum 1840
                    background Solid("#101827ee")
                    padding (18, 10)

                    text toast[1]:
                        color "#f6f7fb"
                        size 22
                        layout "nobreak"
                        text_align 1.0
                        xalign 1.0

screen achievement_list_screen():
    modal True
    zorder 140

    add Solid("#080c14e8")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1040
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 18

            hbox:
                spacing 18
                xalign 0.5
                text "🏆 Conquistas" color "#f5c84b" size 44
                text "%d/%d" % (unlocked_achievement_count(), len(achievement_data)) color "#f6f7fb" size 28 yalign 0.5

            viewport:
                xmaximum 930
                ymaximum 620
                scrollbars "vertical"
                mousewheel True

                vbox:
                    spacing 10

                    for achievement in achievement_data:
                        $ unlocked = achievement_unlocked(achievement["id"])
                        frame:
                            xfill True
                            background Solid("#26324a" if unlocked else "#1c2435")
                            padding (18, 14)

                            hbox:
                                spacing 16
                                yalign 0.5
                                text ("🏆" if unlocked else "🔒") color ("#f5c84b" if unlocked else "#7f8797") size 30 yalign 0.5
                                vbox:
                                    spacing 4
                                    text (achievement["name"] if unlocked else "???") color ("#ffffff" if unlocked else "#7f8797") size 25
                                    text achievement["description"] color ("#cfd7e6" if unlocked else "#8a93a5") size 19

            textbutton _("Fechar") action Hide("achievement_list_screen") xalign 0.5

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

screen gate_notice(title, needed, hint, target_person="", show_date_hint=False, state_text=""):
    modal True
    zorder 110

    default target_label = progress_label(person=target_person) if target_person else progress_label()
    default target_owner = possessive_name(target_person) if target_person else ""

    add Solid("#070b13dd")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1040
        background Solid("#182033")
        padding (42, 36)

        vbox:
            spacing 18
            text title color "#ffffff" size 42 xalign 0.5 text_align 0.5
            text hint color "#dfe7f3" size 28 xmaximum 920 xalign 0.5 text_align 0.5
            if show_date_hint:
                text _("Agora vocês podem sair em encontros ♡ Que fofos!") color "#dfe7f3" size 24 xmaximum 920 xalign 0.5 text_align 0.5
            if state_text:
                text state_text color "#f0a7bb" size 26 xmaximum 920 xalign 0.5 text_align 0.5
            elif target_person:
                text _("[target_label] [target_owner]: [needed]") color "#f0a7bb" size 26 xmaximum 920 xalign 0.5 text_align 0.5
            else:
                text _("[target_label] necessário: [needed]") color "#f0a7bb" size 26 xmaximum 920 xalign 0.5 text_align 0.5
            textbutton _("Abrir dia a dia") action Return(True) xalign 0.5

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

            text _("Dia a dia") color pov_color() size 46 xalign 0.5
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
                                text "%s %s" % (loc.get("emoji", ""), loc["name"]) color ("#ffffff" if loc_ready else "#7f8797") size 32 xalign 0.5
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
                        text _("➡️ Continuar história") color ("#ffffff" if continue_ready else "#7f8797") size 32 xalign 0.5
                        if stage != "primeiro_contato":
                            text free_time_continue_hint(stage, needed, target_person) color ("#f7d7e2" if continue_ready else "#a2a9b8") size 20 xalign 0.5 text_align 0.5
                            if continue_ready and continue_will_pass_time(stage):
                                text _("Isso passará o tempo.") color "#cfd7e6" size 18 xalign 0.5 text_align 0.5

screen endgame_location_picker():
    modal True
    zorder 70

    default locked_location_id = None
    default locked_location_hint = ""

    add Solid(free_turn_overlay())

    frame:
        xalign 0.5
        yalign 0.5
        background Solid(pov_dark())
        padding (34, 30)

        vbox:
            spacing 18

            text _("Dia a dia") color pov_color() size 46 xalign 0.5
            text _("🏆 História concluída, mas você pode continuar jogando infinitamente nesse modo para rever eventos, ver o que tiver perdido ou caçar todas as conquistas.") color "#f5c84b" size 23 xmaximum 1120 xalign 0.5 text_align 0.5

            grid 2 4:
                spacing 16
                xalign 0.5

                for loc in location_data:
                    if loc["id"] in unlocked_locations:
                        $ loc_id = loc["id"]
                        $ loc_ready = location_available(loc["id"])
                        $ bandejao_closed = loc_id == "bandejao" and not bandejao_is_open()
                        button:
                            xsize 540
                            ysize 118
                            background Solid("#232d42" if loc_ready else "#202532")
                            hover_background Solid("#33405d" if loc_ready else "#2b3140")
                            action If(loc_ready, Return(loc_id), [SetScreenVariable("locked_location_id", loc_id), SetScreenVariable("locked_location_hint", locked_location_message(loc_id))])

                            vbox:
                                spacing 5
                                xalign 0.5
                                yalign 0.5
                                text "%s %s" % (loc.get("emoji", ""), loc["name"]) color ("#ffffff" if loc_ready else "#7f8797") size 29 xalign 0.5
                                if loc_id == "bandejao":
                                    if bandejao_closed:
                                        text _("O bandejão está fechado agora.") color "#a2a9b8" size 18 xalign 0.5
                                    else:
                                        text _("Gasta R$ 2,00") color ("#f7d7e2" if loc_ready else "#a2a9b8") size 18 xalign 0.5
                                if (not loc_ready) and (not bandejao_closed) and locked_location_id == loc_id and locked_location_hint:
                                    text locked_location_hint color "#f7d7e2" size 17 xalign 0.5 text_align 0.5

                button:
                    xsize 540
                    ysize 118
                    background Solid("#232d42")
                    hover_background Solid("#33405d")
                    action Return("switch_pov")
                    text _("🔁 Trocar POV") color "#ffffff" size 29 xalign 0.5 yalign 0.5

                button:
                    xsize 540
                    ysize 118
                    background Solid("#232d42")
                    hover_background Solid("#33405d")
                    action Return("memories")
                    text _("📖 Reviver memórias") color "#ffffff" size 29 xalign 0.5 yalign 0.5

                button:
                    xsize 540
                    ysize 118
                    background Solid("#232d42")
                    hover_background Solid("#33405d")
                    action Return("configure")
                    text _("⚙️ Configurar estado") color "#ffffff" size 29 xalign 0.5 yalign 0.5

screen endgame_memory_screen():
    modal True
    zorder 120

    add Solid("#080c14f2")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1040
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 18
            text _("Reviver memórias") color "#ffffff" size 42 xalign 0.5

            grid 2 6:
                spacing 12
                xalign 0.5

                for memory in endgame_memory_data:
                    button:
                        xsize 450
                        ysize 74
                        background Solid("#232d42")
                        hover_background Solid("#33405d")
                        action Return(memory["label"])
                        text memory["name"] color "#ffffff" size 22 xalign 0.5 yalign 0.5 text_align 0.5

            textbutton _("Voltar") action Return("back") xalign 0.5

screen endgame_state_screen():
    modal True
    zorder 120

    add Solid("#080c14f2")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1040
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 18
            text _("Configurar estado") color "#ffffff" size 42 xalign 0.5
            text _("Use para testar variações de POV, país, carreira e fase do dia a dia.") color "#cfd7e6" size 23 xmaximum 900 xalign 0.5 text_align 0.5

            grid 2 3:
                spacing 12
                xalign 0.5

                for state in endgame_state_data:
                    button:
                        xsize 450
                        ysize 92
                        background Solid("#232d42")
                        hover_background Solid("#33405d")
                        action Return(state)
                        text state["name"] color "#ffffff" size 22 xalign 0.5 yalign 0.5 text_align 0.5

            textbutton _("Voltar") action Return("back") xalign 0.5

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
    zorder 60

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
                if gift_is_visible(gift):
                    $ gift_ready = gift_is_available(gift)
                    button:
                        xfill True
                        ysize 92
                        background Solid("#232d42" if gift_ready else "#202532")
                        hover_background Solid("#33405d" if gift_ready else "#202532")
                        sensitive gift_ready
                        action Return(gift["id"])

                        fixed:
                            xfill True
                            yfill True

                            text "%s %s" % (gift.get("emoji", ""), gift["name"]) color ("#ffffff" if gift_ready else "#7f8797") size 21 xpos 20 xsize 400 yalign 0.5
                            text format_money(gift["cost"]) color ("#f0a7bb" if gift_ready else "#7f8797") size 21 xpos 430 xsize 112 text_align 0.5 yalign 0.5 layout "nobreak"
                            text "+%d %s" % (gift["love"], progress_label(person=other_pov())) color ("#89c7f5" if gift_ready else "#7f8797") size 20 xpos 550 xsize 185 text_align 0.5 yalign 0.5
                            text gift_status_text(gift) color ("#cbd5e1" if gift_ready else "#a2a9b8") size 17 xpos 752 xsize 300 yalign 0.5

            textbutton _("Voltar") action Return("back") xalign 0.5

screen photo_gift_difficulty_screen():
    modal True
    zorder 60

    add Solid("#080c14f2")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 980
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 22
            xalign 0.5

            text _("Presente com fotos") color "#ffffff" size 44 xalign 0.5 text_align 0.5
            text _("Escolha o tamanho do mosaico. Se pular, o capricho vale metade.") color "#cfd7e6" size 24 xmaximum 820 xalign 0.5 text_align 0.5

            hbox:
                spacing 18
                xalign 0.5

                for key in ["facil", "medio", "dificil"]:
                    $ difficulty = photo_gift_difficulties[key]
                    button:
                        xsize 250
                        ysize 140
                        background Solid("#232d42")
                        hover_background Solid("#33405d")
                        action Return(key)

                        vbox:
                            spacing 8
                            xalign 0.5
                            yalign 0.5
                            text difficulty["name"] color "#ffffff" size 30 xalign 0.5
                            text "%dx%d" % (difficulty["size"], difficulty["size"]) color "#cfd7e6" size 22 xalign 0.5
                            text "+%d %s" % (difficulty["reward"], progress_label(person=other_pov())) color "#89c7f5" size 22 xalign 0.5

            textbutton _("Voltar") action Return("back") xalign 0.5

screen sliding_photo_puzzle(photo, pieces, size, difficulty_name, piece_displays):
    modal True
    zorder 60

    default puzzle_layout = photo_puzzle_layout(photo, size)
    default tile_width = puzzle_layout["tile_width"]
    default tile_height = puzzle_layout["tile_height"]

    add Solid("#080c14f2")

    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#151c2c")
        padding (28, 24)

        vbox:
            spacing 18
            xalign 0.5

            text _("Monte o mosaico - [difficulty_name]") color "#ffffff" size 38 xalign 0.5

            grid size size:
                spacing 2
                xalign 0.5

                for index, piece in enumerate(pieces):
                    if piece == len(pieces) - 1:
                        button:
                            xysize (tile_width, tile_height)
                            background Solid("#0d1117")
                            action NullAction()
                    else:
                        button:
                            xysize (tile_width, tile_height)
                            background Solid("#0d1117")
                            hover_background Solid("#1f6feb44")
                            action [Function(puzzle_move_in_place, pieces, index, size), Function(renpy.restart_interaction)]

                            add piece_displays[piece] xysize (tile_width, tile_height)

            hbox:
                spacing 18
                xalign 0.5

                textbutton _("Pular"):
                    action Return(("skip", None))

                if puzzle_solved(pieces):
                    textbutton _("Finalizar"):
                        action Return(("done", None))

screen rhythm_song_screen():
    modal True
    zorder 120

    add Solid("#080c14f2")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 900
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 22
            xalign 0.5

            text _("Escolha a música") color "#ffffff" size 44 xalign 0.5
            text _("Jogue uma música para desbloquear a próxima.") color "#cfd7e6" size 24 xalign 0.5 text_align 0.5

            for entry in rhythm_song_entries():
                $ track_id = entry["track_id"]
                $ track = rhythm_tracks[track_id]
                $ song_ready = not entry["locked"]
                button:
                    xsize 720
                    ysize 92
                    background Solid("#232d42" if song_ready else "#202532")
                    hover_background Solid("#33405d" if song_ready else "#202532")
                    action If(song_ready, Return(track_id), Function(rhythm_locked_song_press, track_id))

                    vbox:
                        spacing 5
                        yalign 0.5
                        xalign 0.5
                        text track["title"] color ("#ffffff" if song_ready else "#7f8797") size 30 xalign 0.5
                        if song_ready:
                            text track["artist"] color "#cfd7e6" size 20 xalign 0.5
                        else:
                            text entry["message"] color "#a2a9b8" size 20 xalign 0.5

screen rhythm_difficulty_screen(track_id):
    modal True
    zorder 120

    add Solid("#080c14f2")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 980
        background Solid("#151c2c")
        padding (34, 30)

        vbox:
            spacing 18
            xalign 0.5

            text rhythm_tracks[track_id]["title"] color "#ffffff" size 44 xalign 0.5
            text _("Escolha a dificuldade") color "#cfd7e6" size 24 xalign 0.5

            grid 2 3:
                spacing 14
                xalign 0.5

                for chart in sm_charts(track_id):
                    $ chart_ready = rhythm_chart_unlocked(track_id, chart)
                    button:
                        xsize 360
                        ysize 116
                        background Solid("#232d42" if chart_ready else "#202532")
                        hover_background Solid("#33405d" if chart_ready else "#202532")
                        action If(chart_ready, Return(chart), Function(rhythm_locked_difficulty_press, track_id, chart))

                        vbox:
                            spacing 4
                            xalign 0.5
                            yalign 0.5
                            text chart["difficulty"] color ("#ffffff" if chart_ready else "#7f8797") size 28 xalign 0.5
                            text _("Nível %s" % chart["meter"]) color ("#cfd7e6" if chart_ready else "#7f8797") size 20 xalign 0.5
                            text rhythm_chart_result_text(chart) color ("#f7d7e2" if chart_ready else "#7f8797") size 18 xalign 0.5

screen rhythm_game_screen():
    modal True
    zorder 125

    timer 0.03 repeat True action [Function(rhythm_update), If(rhythm_state.get("done"), Return(True), Function(renpy.restart_interaction))]

    key "K_LEFT" action [Function(rhythm_hit, "left"), Function(renpy.restart_interaction)]
    key "K_DOWN" action [Function(rhythm_hit, "down"), Function(renpy.restart_interaction)]
    key "K_UP" action [Function(rhythm_hit, "up"), Function(renpy.restart_interaction)]
    key "K_RIGHT" action [Function(rhythm_hit, "right"), Function(renpy.restart_interaction)]

    add Solid("#070b13f4")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 820
        background Solid("#111827")
        padding (32, 28)

        vbox:
            spacing 16
            xalign 0.5

            text "%s - %s" % (rhythm_state["title"], rhythm_state["difficulty"]) color "#ffffff" size 36 xalign 0.5

            hbox:
                spacing 34
                xalign 0.5
                text _("Score %d" % rhythm_state["score"]) color "#cfd7e6" size 22
                text _("Combo %d" % rhythm_state["combo"]) color "#cfd7e6" size 22
                text rhythm_state["judgement"] color pov_color() size 22

            fixed:
                xysize (760, 640)
                xalign 0.5

                add Solid("#0b1020")

                for lane in rhythm_lanes:
                    vbox:
                        xpos lane["x"]
                        xanchor 0.5
                        ypos 0
                        ysize 640
                        add Solid("#1f293755") xsize 88 ysize 640

                    add rhythm_receptor_display(lane["id"]):
                        xpos lane["x"]
                        ypos 42
                        xanchor 0.5
                        xysize (78, 78)

                add Solid("#f0a7bb66") xpos 76 ypos 81 xsize 596 ysize 4

                for effect in rhythm_visible_hit_effects():
                    add rhythm_hit_display(effect["lane"]):
                        xpos effect["x"]
                        ypos 32
                        xanchor 0.5
                        xysize (98, 98)

                for note in rhythm_visible_notes():
                    add rhythm_arrow_display(note["lane"]):
                        xpos note["x"]
                        ypos note["y"]
                        xanchor 0.5
                        xysize (64, 64)

            text _("Use as setas do teclado.") color "#cfd7e6" size 22 xalign 0.5

label change_pov(who, title=""):
    $ current_pov = who
    $ play_bgm(bgm_for_pov())
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

    while progress_for(gate_person) < needed:
        call free_time_phase(gate_name, needed, gate_person, hint) from _call_free_time_phase

    return

label free_time_phase(stage="campus", needed=0, target_person=None, blocked_hint=None):
    $ set_love_cap_stage(stage)
    $ apply_free_time_start(stage)
    $ play_bgm("daily_light")
    if free_time_has_continue_requirements(stage, needed, target_person) and not free_time_can_continue(stage, needed, target_person):
        $ gate_person = target_person or resolved_continue_requirements(stage, needed, target_person).get("person", other_pov())
        $ gate_state_text = free_time_continue_hint(stage, needed, target_person)
        $ show_date_hint = stage == "pedido_namoro" and not date_gate_notice_seen
        call screen gate_notice(_("Memória bloqueada"), needed, free_time_blocked_hint(stage, blocked_hint), gate_person, show_date_hint, gate_state_text)
        if show_date_hint:
            $ date_gate_notice_seen = True
    $ keep_looping = True

    while keep_looping:
        $ play_bgm("daily_light")
        window hide
        $ show_free_turn_scene()
        call screen location_picker(stage, needed, target_person)
        window auto
        $ selected_location = _return

        if selected_location == "continue":
            $ advance_to_story_day(stage)
            $ keep_looping = False
        elif selected_location == "poli":
            call poli_interaction(stage) from _call_poli_interaction
        elif selected_location == "bandejao":
            $ paid_bandejao = spend_money(2, "bandejão")
            if paid_bandejao:
                call bandejao_interaction(stage) from _call_bandejao_interaction
        elif selected_location == "heitor_home":
            call heitor_home_interaction(stage) from _call_heitor_home_interaction
        elif selected_location == "shop":
            call gift_phase(stage) from _call_gift_phase
        elif selected_location == "work":
            if stage == "primeiro_contato":
                call mother_money_phase(stage) from _call_mother_money_phase
            else:
                call money_phase(stage) from _call_money_phase

    return

label endgame_loop:
    $ endgame_mode = True
    $ endgame_replay_mode = False
    $ unlock_achievement("endgame_mode")
    $ play_bgm("endgame")
    $ special_day_label = "🏆 Pós-jogo"
    $ first_kiss_done = True
    $ dating_started = True
    $ unlocked_locations = ["poli", "bandejao", "heitor_home", "shop", "work"]
    show screen relationship_hud

    while True:
        $ play_bgm("endgame")
        window hide
        $ show_free_turn_scene()
        call screen endgame_location_picker
        window auto
        $ selected_location = _return
        $ endgame_stage = current_love_cap_stage

        if selected_location == "poli":
            call poli_interaction(endgame_stage) from _call_poli_interaction_1
        elif selected_location == "bandejao":
            $ paid_bandejao = spend_money(2, "bandejão")
            if paid_bandejao:
                call bandejao_interaction(endgame_stage) from _call_bandejao_interaction_1
        elif selected_location == "heitor_home":
            call heitor_home_interaction(endgame_stage) from _call_heitor_home_interaction_1
        elif selected_location == "shop":
            call gift_phase(endgame_stage) from _call_gift_phase_1
        elif selected_location == "work":
            call money_phase(endgame_stage) from _call_money_phase_1
        elif selected_location == "switch_pov":
            $ next_pov = other_pov()
            call quick_change_pov(next_pov) from _call_quick_change_pov
        elif selected_location == "memories":
            call screen endgame_memory_screen
            $ memory_label = _return
            if memory_label != "back":
                call endgame_replay_memory(memory_label) from _call_endgame_replay_memory
        elif selected_location == "configure":
            call screen endgame_state_screen
            $ state = _return
            if state != "back":
                $ current_pov = state["pov"]
                $ current_country_label = state["country"]
                $ career_phase = state["career"]
                $ set_love_cap_stage(state["stage"])
                $ first_kiss_done = True
                $ dating_started = True
                $ queue_notification("Estado ajustado para testar variações.")

    return

label endgame_replay_memory(memory_label):
    $ endgame_replay_mode = True
    $ unlock_achievement("endgame_memory_replay")
    call expression memory_label from _call_expression
    $ endgame_replay_mode = False
    $ special_day_label = "🏆 Pós-jogo"
    show screen relationship_hud
    return

label endgame_intro_replay:
    call change_pov("heitor", "Uma rara ida ao Bandejão Central") from _call_change_pov

    scene bg bandejao
    with fade

    show heitor college neutral at pov_left
    show ana college neutral at other_right

    a "Engraçado… a gente é da mesma sala há meses."

    show heitor college soft_smile
    h "Pois é."

    ana_thought "Ficamos conversando o jantar inteiro. Me dissociei um pouco dos arredores."

    ana_thought "Todos os amigos conversavam entre si, mas havia algo me impedindo de olhar em outra direção."

    ana_thought "Talvez um pouco mais. Ele era tão fofo..."

    return

label ana_distance_missing_beat(stage, love=3, reason="saudade da presença"):
    ana_thought "No fim, a parte mais estranha era perceber o espaço exato que ele ocupava quando estava por perto."
    ana_thought "Eu sentia falta dele ali."
    $ add_partner_love(love, reason)
    $ advance_free_time(stage)
    return

label ana_distance_poli_interaction(stage="campus"):
    $ play_bgm("ana_sad")
    $ show_free_action_scene("bg desktop_code")
    with fade

    show ana college thinking at pov_left

    menu:
        "Resolver uma lista sozinha":
            a "Ok. Uma lista, uma Ana e zero Heitor para falar que isso é tranquilo."
            ana_thought "Eu abri uma conversa antiga nossa só para lembrar do jeito que ele explicava as coisas."
            ana_thought "A resposta não veio dali, mas a calma um pouco sim."
            call ana_distance_missing_beat(stage, 4, "lista com saudade") from _call_ana_distance_missing_beat

        "Fazer debug do EP":
            call ana_distance_debug_ep(stage) from _call_ana_distance_debug_ep

        "Reclamar da Poli":
            a "Hoje a reclamação vai ter que ser em formato monólogo."
            ana_thought "Era ridículo como até reclamar da graduação ficava melhor quando ele estava do lado."
            call ana_distance_missing_beat(stage, 3, "reclamação em modo saudade") from _call_ana_distance_missing_beat_1

    return

label ana_distance_bandejao_interaction(stage="campus"):
    $ play_bgm("ana_sad")
    $ show_free_action_scene("bg bandejao")
    with fade

    show ana college neutral at pov_left

    menu:
        "Bandejão speedrun":
            a "Eu fui na Física só porque era mais perto."
            show ana college annoyed
            a "O arroz continua duro. Ele ia estar feliz. Eu, menos."
            call ana_distance_missing_beat(stage, 4, "Física sem Heitor") from _call_ana_distance_missing_beat_2

        "Comida barata e conversa boa":
            a "O prato até estava bom."
            ana_thought "Mas a mesa parecia grande demais para uma pessoa só."
            call ana_distance_missing_beat(stage, 4, "bandejão sem companhia") from _call_ana_distance_missing_beat_3

        "Debater o ranking dos bandejões":
            a "Central é melhor. Isso nem é debate."
            ana_thought "Eu quase mandei mensagem para ele só para brigar com a defesa absurda da Física."
            call ana_distance_missing_beat(stage, 3, "ranking à distância") from _call_ana_distance_missing_beat_4

    return

label ana_distance_home_interaction(stage="home"):
    $ play_bgm("ana_sad")
    $ show_free_action_scene(bedroom_background())
    with fade

    show ana home neutral at pov_left

    menu:
        "Assistir algo no sofá":
            a "Hoje eu vou entender a história."
            pause 0.4
            show ana home sad
            a "Ou vou pausar no meio porque não tem ninguém para eu perguntar o que está acontecendo."
            call ana_distance_missing_beat(stage, 5, "sofá com lugar sobrando") from _call_ana_distance_missing_beat_5

        "Jogar alguma coisa":
            menu:
                "Jogo de habilidade":
                    call rhythm_skill_phase(stage) from _call_rhythm_skill_phase
                    ana_thought "Ganhar era legal. Ter ele rindo do meu desespero teria sido melhor."

                "Jogo de história":
                    a "É tipo um filme, só que com botão."
                    ana_thought "Eu conseguia ouvir ele respondendo que isso era justamente a melhor parte."
                    call ana_distance_missing_beat(stage, 3, "filme com botão sem debate") from _call_ana_distance_missing_beat_6

                "Jogo de aventura":
                    a "Se eu cair aqui, ninguém vai falar 'pula agora' com toda a confiança do mundo."
                    ana_thought "Que ódio. Eu sentia falta até disso."
                    call ana_distance_missing_beat(stage, 4, "aventura em modo solo") from _call_ana_distance_missing_beat_7

        "Cozinhar algo barato (R$ 10,00)" if current_money() >= 10:
            $ spend_money(10, "jantar barato")
            a "A receita tem três passos."
            show ana home embarrassed
            a "Eu errei em quatro mesmo sem ele aqui para chamar de versão beta."
            call ana_distance_missing_beat(stage, 4, "jantar improvisado à distância") from _call_ana_distance_missing_beat_8

        "Pedir Tavares no iFood (R$ 18,00)" if current_money() >= 18:
            $ spend_money(18, "Tavares no iFood")
            a "Frango parmegiana do Tavares."
            show ana home neutral
            a "Ele defenderia isso com argumentos econômicos muito fortes."
            ana_thought "Eu ainda não entendia totalmente. Mas entendia a saudade."
            call ana_distance_missing_beat(stage, 3, "Tavares sem advogado") from _call_ana_distance_missing_beat_9

    return

label ana_distance_debug_ep(stage="campus"):
    $ score = 0
    $ play_bgm("study_debug")

    system_line "Debug do EP. Agora com chamada mental de suporte técnico ausente."

    $ code_puzzle = pick_code_bug_puzzle()
    call screen code_bug_screen(code_puzzle)
    $ selected_code_line = _return

    if selected_code_line == code_puzzle["answer"]:
        $ score += 2
        $ code_result_text = code_puzzle["success"]
    else:
        $ code_result_text = code_puzzle["failure"]

    system_line "[code_result_text]"

    if score >= 2:
        show ana college soft
        a "Tá. Eu consegui."
        ana_thought "Eu queria poder mandar a tela para ele e fingir que era só pelo EP."
        call ana_distance_missing_beat(stage, 6, "debug com saudade") from _call_ana_distance_missing_beat_10
    else:
        show ana college embarrassed
        a "Não resolveu tudo."
        ana_thought "E a cadeira vazia do lado não ajudou em nada."
        call ana_distance_missing_beat(stage, 3, "debug sem dupla") from _call_ana_distance_missing_beat_11

    return

label poli_interaction(stage="campus"):
    if ana_distance_day(stage):
        call ana_distance_poli_interaction(stage) from _call_ana_distance_poli_interaction
        return

    $ play_bgm("study_debug")
    $ show_free_action_scene("bg desktop_code")
    with fade

    if current_pov == "heitor":
        show heitor focused at pov_left
        show ana college thinking at other_right
    else:
        show ana college thinking at pov_left
        if not ana_distance_day(stage):
            show heitor focused at other_right

    $ poli_complaint_label = "Ouvir reclamação da Poli" if current_pov == "heitor" else "Reclamar da Poli"

    menu:
        "Resolver uma lista juntos":
            a "Se a gente dividir por questão, talvez dê tempo."
            h "Ou a gente descobre que a questão 20 depende da 19, que depende da 18, que depende da 17, que depende da 16..."
            show ana college annoyed
            a "N-Não brinca com esse tipo de coisa!!!"
            $ add_partner_love(4, "lista em dupla")
            $ advance_free_time(stage)

        "Fazer debug do EP":
            call minigame_debug_ep(stage) from _call_minigame_debug_ep

        "[poli_complaint_label]":
            system_line "A Ana fica 20 minutos reclamando de como ela não leva jeito pra computação."
            show ana college happy
            a "Reclamar deixa tudo um pouco menos pior."
            show heitor college amused
            h "Na Poli isso quase conta como atividade complementar."
            $ add_partner_love(3, "reclamação acadêmica")
            $ advance_free_time(stage)

    return

label bandejao_interaction(stage="campus"):
    if ana_distance_day(stage):
        call ana_distance_bandejao_interaction(stage) from _call_ana_distance_bandejao_interaction
        return

    $ play_bgm("daily_light")
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
            call minigame_bandejao(stage) from _call_minigame_bandejao

        "Comida barata e conversa boa":
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
    if ana_distance_day(stage):
        call ana_distance_home_interaction(stage) from _call_ana_distance_home_interaction
        return

    $ play_bgm("game_fun")
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
            menu:
                "Jogo de habilidade":
                    call rhythm_skill_phase(stage) from _call_rhythm_skill_phase_1

                "Jogo de história":
                    a "Esse jogo é meio chato."
                    h "Chato?"
                    a "É tipo um filme, só que pior."
                    h "Você quer dizer: tipo um filme, só que melhor."
                    show ana college annoyed
                    a "Eu sabia que você ia defender."
                    $ add_partner_love(3, "jogo de história")
                    $ advance_free_time(stage)

                "Jogo de aventura":
                    a "Eu aviso desde já que eu vou gritar se tiver que pular em alguma coisa."
                    h "Então vai ser um jogo de aventura bem barulhento."
                    show ana college happy
                    a "E você vai falar 'pula agora' como se isso ajudasse."
                    h "Vai ajudar quando você pular."
                    a "Eu vou estar pulando!"
                    $ add_partner_love(4, "jogo de aventura")
                    $ advance_free_time(stage)

        "Cozinhar algo barato (R$ 10,00)" if current_money() >= 10:
            $ spend_money(10, "jantar barato")
            h "A receita tem três passos."
            a "Então em algum momento vamos errar quatro."
            h "Se der errado, a gente chama de versão beta."
            show ana college happy
            a "Desde que a versão beta seja comestível."
            $ add_partner_love(4, "jantar improvisado")
            $ advance_free_time(stage)

        "Pedir Tavares no iFood (R$ 18,00)" if current_money() >= 18:
            $ spend_money(18, "Tavares no iFood")
            h "Frango parmegiana do Tavares?"
            show ana college neutral
            a "Você gosta disso num nível que eu nunca vou entender."
            h "É barato, vem bastante e resolve o jantar. Três requisitos, três aprovações."
            show ana college happy
            a "Tá bom. Não é meu favorito, mas dá pra viver."
            heitor_thought "Vitória absoluta do custo-benefício."
            $ add_partner_love(3, "parmegiana do Tavares")
            $ advance_free_time(stage)

    return

label rhythm_skill_phase(stage="home"):
    $ rhythm_play_count += 1
    call screen rhythm_song_screen
    $ rhythm_track_id = _return

    call screen rhythm_difficulty_screen(rhythm_track_id)
    $ rhythm_chart = _return
    $ rhythm_charts_for_track = sm_charts(rhythm_track_id)
    if rhythm_charts_for_track and rhythm_chart["id"] == rhythm_charts_for_track[-1]["id"]:
        $ unlock_achievement("ddr_master")

    $ start_rhythm_state(rhythm_track_id, rhythm_chart)
    $ renpy.music.play(rhythm_tracks[rhythm_track_id]["music"], channel="music", loop=False)
    call screen rhythm_game_screen
    $ renpy.music.stop(channel="music", fadeout=0.5)
    $ play_bgm("game_fun", fadein=1.0, fadeout=0.0)

    $ rhythm_points = rhythm_reward()
    $ rhythm_acc = rhythm_accuracy()
    $ rhythm_record_result(rhythm_chart)
    if rhythm_acc >= 98:
        $ unlock_achievement("rhythm_perfect")
    $ rhythm_unlock_next_song(rhythm_track_id)
    $ rhythm_unlock_next_chart(rhythm_track_id, rhythm_chart)

    if ana_distance_day(stage):
        if rhythm_acc >= 85:
            show ana college super_happy
            a "Eu apertei coisa demais e funcionou!"
            ana_thought "Ele ia fazer uma cara orgulhosa idiota. Eu senti falta exatamente dessa cara."
        elif rhythm_acc >= 55:
            show ana college happy
            a "Não foi perfeito, mas foi divertido."
            ana_thought "Faltou ele cantar alguma coisa fora de hora."
        else:
            show ana college embarrassed
            a "Eu acho que dancei mais com a cara do que com os dedos."
            ana_thought "E nem tinha ele aqui para transformar o desastre em piada."
    elif rhythm_acc >= 85:
        h "Ok, isso foi bonito."
        show ana college super_happy
        a "Eu apertei coisa demais e funcionou!"
    elif rhythm_acc >= 55:
        show ana college happy
        a "Não foi perfeito, mas foi divertido."
        h "🎵 Din don, din don dan 🎵."
    else:
        show ana college embarrassed
        a "Eu acho que dancei mais com a cara do que com os dedos."
        h "Ainda conta como cardio."

    $ add_partner_love(rhythm_points, "jogo de habilidade")
    $ advance_free_time(stage)
    return

label gift_phase(stage="shop"):
    $ play_bgm("daily_light")
    $ show_free_action_scene("bg desktop_code")
    with fade

    call screen gift_shop_screen
    $ gift_id = _return

    if gift_id == "back":
        return

    $ gift = gift_by_id(gift_id)

    if gift is None:
        return

    if gift_id == "photo_gift":
        call photo_gift_phase(stage, gift) from _call_photo_gift_phase
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
        if gift_id not in purchased_gifts:
            $ purchased_gifts.append(gift_id)
        if gift_id == "earrings":
            $ unlock_achievement("earrings_bought")
        if gift_id == "sushi_date":
            $ unlock_achievement("daily_sushi")
        $ add_partner_love(gift_love, gift_name)
        $ advance_free_time(stage)
        if ana_distance_day(stage) and gift_id == "sushi_date":
            show ana college neutral at pov_left
            a "Eu fui comer sushi sozinha."
            show ana college sad
            a "Continuava gostoso."
            ana_thought "Mas ninguém estava ali para trocar salmão grelhado por sashimi comigo."
            ana_thought "A cadeira vazia parecia saber exatamente o quanto eu sentia falta dele."
        elif ana_distance_day(stage):
            system_line "Você separou para mandar depois: [gift_name]."
            ana_thought "A graça era imaginar a reação dele. A parte difícil era não ter essa reação na minha frente."
        else:
            system_line "Você entregou: [gift_name]."
    else:
        system_line "A carteira olhou para o preço e pediu análise assintótica."

    return

label photo_gift_phase(stage="shop", gift=None):
    call screen photo_gift_difficulty_screen
    $ difficulty_id = _return

    if difficulty_id == "back":
        return

    $ photo_path = pick_gift_photo()
    if photo_path is None:
        system_line "As fotos ainda não foram encontradas. O presente ficou no mundo das ideias por enquanto."
        return

    $ gift_name = gift["name"]
    $ gift_cost = gift["cost"]
    $ bought_gift = spend_money(gift_cost, gift_name)

    if not bought_gift:
        system_line "A carteira olhou para o preço e pediu análise assintótica."
        return

    $ difficulty = photo_gift_difficulties[difficulty_id]
    $ puzzle_size = difficulty["size"]
    $ puzzle_reward = difficulty["reward"]
    $ difficulty_name = difficulty["name"]
    $ puzzle_pieces = shuffled_photo_puzzle(puzzle_size, difficulty["moves"])
    $ puzzle_piece_displays = photo_puzzle_piece_displays(photo_path, puzzle_size)
    $ skipped_puzzle = False

    if ana_distance_day(stage):
        system_line "Você separa as fotos, tenta fazer um mosaico bonito e descobre que saudade também tem complexidade combinatória."
    else:
        system_line "Você separa as fotos, tenta fazer um mosaico bonito e descobre que romantismo também tem complexidade combinatória."

    call screen sliding_photo_puzzle(photo_path, puzzle_pieces, puzzle_size, difficulty_name, puzzle_piece_displays)
    $ puzzle_action, puzzle_index = _return
    if puzzle_action == "skip":
        $ skipped_puzzle = True
        $ puzzle_pieces = list(range(puzzle_size * puzzle_size))

    scene black
    show expression scaled_photo_display(photo_path, puzzle_size) as completed_photo at truecenter
    with dissolve
    pause 1.5

    if skipped_puzzle:
        $ final_reward = max(1, int(puzzle_reward / 2))
        system_line "Ficou meio torto, mas foi feito com carinho. Meio esforço, metade do brilho."
    else:
        $ final_reward = puzzle_reward
        system_line "O mosaico fecha certinho. Presente barato, capricho caríssimo."

    if ana_distance_day(stage):
        ana_thought "Eu queria ver ele olhando as fotos comigo, apontando alguma lembrança boba que eu quase tinha esquecido."
        ana_thought "A foto mostrava uma memória de nós dois. O quarto, não."

    hide completed_photo
    $ photo_gift_completed = True
    $ photo_gift_completion_count += 1
    $ unlock_achievement("photo_gift")
    if difficulty_id == "dificil":
        $ unlock_achievement("photo_gift_hard")
    if photo_gift_completion_count >= 5:
        $ unlock_achievement("photo_gift_five")
    if not skipped_puzzle:
        $ unlock_achievement("photo_no_skip")
    $ inventory.append(gift_name)
    $ add_partner_love(final_reward, gift_name)
    $ advance_free_time(stage, 2)
    return

label money_phase(stage="money"):
    if not ana_distance_day(stage):
        $ play_bgm("work_money")
    $ show_free_action_scene("bg desktop_code")
    with fade

    if current_pov == "heitor":
        show heitor focused at pov_left
        show ana college thinking at other_right
    else:
        show ana college thinking at pov_left
        show heitor focused at other_right

    if current_pov == "ana":
        menu:
            "Trabalhar na IC":
                a "Eu não fiz quase nada e eles elogiam o que eu fiz como se fosse a melhor coisa do mundo."
                if ana_distance_day(stage):
                    ana_thought "Eu quase mandei para ele: '2h de reunião'."
                    ana_thought "Ele provavelmente ia perguntar se era pesquisa mesmo ou bate-papo."
                    ana_thought "Só imaginar a resposta dele já deixou a sala um pouco menos vazia."
                else:
                    h "Meu Deus, 2h de reunião! Vocês tão pesquisando mesmo ou batendo papo?"
                $ add_money(32, "bolsa de IC")
                $ advance_free_time(stage, 2)

            "Pegar uma janela de estágio":
                call ana_internship_phase(stage) from _call_ana_internship_phase

            "Pedir ajuda para a nanãe":
                call mother_money_phase(stage) from _call_mother_money_phase_1
    else:
        if career_phase != "btg":
            menu:
                "Trabalhar na IC":
                    h "Mais uma noite sem dormir, é hoje que eu termino esse paper."
                    $ add_money(32, "bolsa de IC")
                    $ advance_free_time(stage, 2)

                "Trabalhar para o Crossing":
                    call heitor_crossing_phase(stage) from _call_heitor_crossing_phase
        else:
            menu:
                "Trabalhar na IC":
                    h "Mais uma noite sem dormir, é hoje que eu termino esse paper."
                    $ add_money(32, "bolsa de IC")
                    $ advance_free_time(stage, 2)

    return

label ana_internship_phase(stage="money"):
    $ job = career_data.get(career_phase, career_data["btg"])
    $ job_title = job["title"]

    $ add_money(job["money"], job["reason"])
    $ add_partner_love(job["love"], job["reason"])
    show ana college happy
    a "[job_title]"
    if career_phase == "btg":
        call whatsapp_btg_excerpt from _call_whatsapp_btg_excerpt
        $ show_free_action_scene("bg desktop_code")
        with dissolve
        show ana college happy at pov_left
        if not ana_distance_day(stage):
            show heitor focused at other_right
    elif career_phase == "virtualisurg_frontend":
        if not ana_distance_day(stage):
            h "Nossa, como eu amo front-end, quero trabalhar com isso pro resto da vida."
        show ana college happy
        a "Finalmente centralizei a div, que dia produtivo."
    else:
        if not ana_distance_day(stage):
            h "Muito bem."
        show ana college sad
        a "Que saudade do front..."
    if ana_distance_day(stage):
        ana_thought "Eu queria contar cada detalhe para ele sem depender de fuso, mensagem e horário quebrado."
        ana_thought "No fim do dia, a falta dele fazia mais barulho que qualquer notificação."
    else:
        h "Dinheiro a gente faz..."
        show ana college annoyed
        a "Até parece"

    $ advance_free_time(stage, 2)
    return

label heitor_crossing_phase(stage="money"):
    show heitor focused at pov_left
    show ana college thinking at other_right

    h "Tenho que fazer o paper do Crossing."
    a "Ainda ta nisso, já não tinha acabado?"
    h "Alguém tem que trabalhar nessa casa."
    show ana college happy
    a "Larga isso, já deu."

    $ add_money(70, "plantão no Crossing")
    $ add_partner_love(2, "plantão no Crossing")
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
            $ unlock_achievement("aline_limit")
            system_line "Aline: Que isso Ana, ta passando fome?"
            system_line "Dessa vez o pix não veio. Talvez seja melhor esperar amanhã."
        else:
            $ add_money(200, "Aline salvou o dia")
            system_line "Não demora muito para o pix cair."

        if ana_distance_day(stage):
            ana_thought "Eu queria contar para ele que a nanãe tinha salvado o dia de novo."
            ana_thought "Até uma besteira dessas parecia melhor quando ele estava por perto para rir comigo."
        
        $ advance_free_time(stage)
    else:
        $ show_free_action_scene("bg desktop_code")
        with fade

        show heitor thoughtful at pov_left
        heitor_thought "Pedir dinheiro para a mãe da Ana parece uma permissão que eu definitivamente não tenho."
        $ advance_free_time(stage)

    return

label minigame_bandejao(stage="campus"):
    $ play_bgm("choice_tension")
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
                system_line "Ana que eficiência não compensa comida ruim, mas estar com ele sim."

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
    $ play_bgm("study_debug")

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
