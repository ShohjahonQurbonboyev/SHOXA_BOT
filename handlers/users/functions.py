


def count_time(number):
    barcha_xabarlar_uchun_vaqt = number * 0.8
    soatlar = barcha_xabarlar_uchun_vaqt // 3600
    qoldiq_sekundlar = barcha_xabarlar_uchun_vaqt % 3600
    daqiqalar = qoldiq_sekundlar // 60
    qoldiq_sekundlar = qoldiq_sekundlar % 60
    return int(soatlar), int(daqiqalar), int(qoldiq_sekundlar)
