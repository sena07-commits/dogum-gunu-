import datetime
import requests
import streamlit as st
import time

# 1. Sayfa ayarları (Mutlaka en başta olmalı!)
st.set_page_config(
    page_title="Tilkimin Yuvası", page_icon="🦊", layout="centered"
)

# 2. Ziyaretçi mail bildirimi (Hata ayıklama modlu)
if "bildirim_gonderildi" not in st.session_state:
  st.session_state.bildirim_gonderildi = True
  try:
    zaman = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    url = "https://api.web3forms.com/submit"
    payload = {
        "access_key": "deda9a01-7813-4684-88d1-2550bdcc2bee",
        "subject": "🦊 Tilkimin Yuvası Ziyaret Edildi!",
        "message": f"Sürpriz sitene yeni biri giriş yaptı! Tarih/Saat: {zaman}",
    }
    response = requests.post(url, json=payload, timeout=5)

    if response.status_code == 200:
      st.toast("📧 Bildirim başarıyla gönderildi!", icon="✅")
    else:
      st.warning(f"Mail gönderilemedi, kod: {response.status_code}")
  except Exception as e:
    st.error(f"Bağlantı hatası: {e}")

# (Buradan sonra senin yazdığın parşömen tasarımı, müzik ve aşama kodların aynen devam ediyor...)

# Parşömen / Arka Plan Tasarımı
st.markdown("""
    <style>
    .stApp {
        background-color: #f4ecd8;
        color: #2c221e;
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

# Arka plan müziği
st.audio("sarki.mp3", format="audio/mp3", loop=True)
# OTURUM DURUMU
if "asama" not in st.session_state:
    st.session_state.asama = 1

# AŞAMAYA GÖRE DİNAMİK BAŞLIKLAR
if st.session_state.asama <= 6:
    baslik = "Test"
elif st.session_state.asama == 7:
    baslik = "Gerçek Hayattan Kopmamak İçin Küçük Bir Kesit"
elif st.session_state.asama == 7.5:
    baslik = "🔍 Sistem Analizi"
elif st.session_state.asama == 8:
    baslik = "Emin Misin?"
else:
    baslik = "Doğum Günü Sürprizi"

# HAREKETLİ GÜN DOĞUMU / GÜN BATIMI GEÇİŞLİ ARKA PLAN STİLİ
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #a1c4fd, #c2e9fb);
        background-size: 400% 400%;
        animation: gunDonumuAnimasyon 15s ease infinite;
    }
    
    @keyframes gunDonumuAnimasyon {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    h1, h2, h3, p, label, .stRadio label {
        color: #2c2c2c !important;
        font-family: 'Georgia', serif;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
        color: white !important;
        border: none;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #ff7eb3, #ff758c);
    }
    </style>
""", unsafe_allow_html=True)

# Üst Başlık (Sadece 9. aşama hariç diğer aşamalarda göster)
if st.session_state.asama != 9:
    st.title(baslik)

# 1. SORU (En Sevdiği Renk)
if st.session_state.asama == 1:
    st.subheader("Soru 1: En sevdiğin renk hangisi?")
    cevap1 = st.radio(
        "Seç bakalım:",
        ["Mavi", "Siyah", "Kahverengi", "Bordo", "Beyaz", "Pempe"],
        key="s1",
    )

    if st.button("Sonraki Soruya Geç ➡️"):
        st.session_state.asama = 2
        st.rerun()

# 2. SORU (En Sevdiği Hayvan)
elif st.session_state.asama == 2:
    st.subheader("Soru 2: En sevdiğin hayvan hangisi?")
    
    cevap2 = st.radio(
        "Seç bakalım:",
        [
            "TİLKİ",
            "Vaşak",
            "Kedi",
            "Köpek",
            "Kurt"
        ],
        key="s2",
    )

    if st.button("Sonraki Soruya Geç ➡️"):
        st.session_state.asama = 3
        st.rerun()

# 3. SORU (En Sevdiği Çiçek)
elif st.session_state.asama == 3:
    st.subheader("Soru 3: En sevdiğin çiçek hangisi?")
    
    cevap3 = st.radio(
        "Seç bakalım:",
        [
            "Papatya",
            "Lale",
            "Kasımpatı"
        ],
        key="s3",
    )

    if st.button("Sonraki Soruya Geç ➡️"):
        st.session_state.asama = 4
        st.rerun()

#4. SORU (En Sevdiği Yer)
elif st.session_state.asama == 4:
    st.subheader("Soru 4: En sevdiğin yer neresi?")
    
    cevap4 = st.radio(
        "Seç bakalım:",
        [
            "Çankırı Şabanözü",
            "Park",
            "Ev",
            "Kafe"
        ],
        key="s4",
    )

    if st.button("Sonraki Soruya Geç ➡"):
        st.session_state.asama = 5
        st.rerun()

# 5. SORU (En Sevdiği Yiyecek)
elif st.session_state.asama == 5:
    st.subheader("Soru 5: En sevdiğin yiyecek hangisi?")
    
    cevap5 = st.radio(
        "Seç bakalım:",
        [
            "BAKLAVA",
            "Jelibon",
            "KREMALİ MAKARNA",
            "Brovni",
            "Lelipop"
        ],
        key="s5",
    )

    if st.button("Sonraki Soruya Geç ➡"):
        st.session_state.asama = 6
        st.rerun()

# 6. SORU (En Sevdiği İçecek)
elif st.session_state.asama == 6:
    st.subheader("Soru 6: En sevdiğin içecek hangisi?")
    
    cevap6 = st.radio(
        "Seç bakalım:",
        [
            "Redbull",
            "Tubork",
            "Vişne suyu",
            "Bey pazarı",
            "Tornado",
            "Kola"
        ],
        key="s6",
    )

    if st.button("Sürprizi Aç! 🌸"):
        st.session_state.asama = 7
        st.rerun()

# 7. AŞAMA - SİNEMATİK VİDEO (Siyah Ekran -> Başlık & Video -> Buton)
elif st.session_state.asama == 7:
    st.markdown(
        """
        <style>
        /* Arka planı tamamen siyaha çeviriyoruz */
        .stApp {
            background-color: #000000 !important;
            transition: background-color 2s ease;
        }
        
        /* Başlık ve videonun yavaşça belirme animasyonu */
        @keyframes sinematikBelirme {
            0% { 
                opacity: 0; 
                transform: scale(0.96);
            }
            30% { 
                opacity: 0; /* İlk 1.5 saniye tamamen karanlık kalır */
            }
            100% { 
                opacity: 1; 
                transform: scale(1);
            }
        }
        
        /* En üstteki başlığa da aynı yavaşça belirme efektini veriyoruz */
        h1 {
            animation: sinematikBelirme 4.5s ease-in-out forwards;
        }
        
        .video-kutusu {
            animation: sinematikBelirme 4.5s ease-in-out forwards;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        
        .buton-kutusu {
            animation: sinematikBelirme 6.5s ease-in-out forwards;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sadece 1. Video (Küçük Prens)
    st.markdown('<div class="video-kutusu">', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=JBIEaB08o_4")
    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Aşamaya Geçiş Butonu
    st.markdown('<div class="buton-kutusu">', unsafe_allow_html=True)
    if st.button("Daha Bitmedi ➡️"):
        st.session_state.asama = 7.5
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 7.5. AŞAMA - SAHTE YÜKLEME VE ANALİZ EKRANI (Yavaşlatılmış)
elif st.session_state.asama == 7.5:
    st.markdown("<br>", unsafe_allow_html=True)
    durum_metni = st.empty()
    ilerleme_cubugu = st.progress(0)

    mesajlar = [
        (20, "Cevapların veritabanına aktarılıyor... 📊", 1.8),
        (45, "Tilki DNA'sı ve uyumluluk oranı hesaplanıyor... 🦊", 2.2),
        (75, "Küçük Prens referansları doğrulanıyor... 🌹", 2.0),
        (99, "Sistem hatası: %99 oranında tespiti yapıldı, tam '%100' olduğu anlaşıldı! 🚨", 3.0),
        (100, "Gerçek bir tilki olduğu anlaşıldı! Son aşamaya geçilebilir. ✨", 2.0)
    ]

    for yuzde, mesaj, bekleme_suresi in mesajlar:
        durum_metni.markdown(f"### {mesaj}")
        ilerleme_cubugu.progress(yuzde)
        time.sleep(bekleme_suresi)

    time.sleep(1.0)
    st.session_state.asama = 8
    st.rerun()

# 8. AŞAMA - SONSUZ TEYİT DÖNGÜSÜ
elif st.session_state.asama == 8:
    if "onay_adimi" not in st.session_state:
        st.session_state.onay_adimi = 1

    st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.onay_adimi == 1:
        st.subheader("🎉 Son kısma gelindi! Gerçekten hazır mısın?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Evet, hazırım! 🚀"):
                st.session_state.onay_adimi = 2
                st.rerun()
        with col2:
            if st.button("Şu an değilim 🏃‍♂️"):
                st.warning("Seçeneklerin arasında bu yok maalesef, devam etmelisin! 😉")

    elif st.session_state.onay_adimi == 2:
        st.subheader("🤔 Emin misin? Bak geri dönüşü yok!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Kesinlikle eminim! 👍"):
                st.session_state.onay_adimi = 3
                st.rerun()
        with col2:
            if st.button("Bir an şüpheye düştüm... 🙃"):
                st.info("Şüpheye yer yok, tırıs tırıs devam ediyorsun! 😄")

    elif st.session_state.onay_adimi == 3:
        st.subheader("🕵️‍♂️ Gerçekten son kararın mı?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Evet, son kararım! 🎯"):
                st.session_state.onay_adimi = 4
                st.rerun()
        with col2:
            if st.button("Biraz düşüneyim 🤔"):
                st.error("Düşünmek yok, süre kısıtlı! Hızlıca 'Evet'e bas.")

    elif st.session_state.onay_adimi == 4:
        st.subheader("🚨 Son kez soruyorum, kalbin bu sürprize dayanabilecek mi?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Dayanır, aç artık! 💥"):
                st.session_state.onay_adimi = 5
                st.rerun()
        with col2:
            if st.button("Pek emin değilim 🫀"):
                st.warning("Yapacak bir şey yok, buraya kadar geldin!")

    elif st.session_state.onay_adimi == 5:
        st.subheader("🦊 Tamamdır, Tilki onay mührünü vurdu. Son kapıyı açıyoruz...")
        if st.button("Aç Kapıyı! ✨"):
            st.session_state.asama = 9
            st.rerun()

# 9. AŞAMA: KAPALI ZARF EKRANI (MUTLU SON)
elif st.session_state.asama == 9:
    import os
    import base64
    
    # Üstteki "Doğum Günü Sürprizi" başlığının finalde görünmemesi için sadece özel başlığımızı kullanıyoruz
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #2c2c2c !important; font-family: 'Georgia', serif; font-size: 28px;">🌹 Ve Mutlu Son...</h1>
        </div>
    """, unsafe_allow_html=True)
    
    img_tag = ""
    try:
        tilki_yolu = "tilki.jpg"
        with open(tilki_yolu, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            img_tag = f'<img src="data:image/jpeg;base64,{encoded}" class="parsomon-foto">'
    except Exception as e:
        img_tag = f'<p style="color:red;">Fotoğraf yüklenemedi: {e}</p>'

    st.markdown("""
        <style>
        .final-kutu {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 10px;
        }
        .zarf-kutusu {
            background: linear-gradient(135deg, #fff6e5, #f5e1be);
            padding: 40px 30px;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(139, 90, 43, 0.25);
            border: 2px solid #d4af37;
            width: 320px;
            text-align: center;
            margin: 0 auto;
        }
        .zarf-ikon {
            font-size: 70px;
            margin-bottom: 15px;
            animation: zarfNefes 2s infinite ease-in-out;
        }
        @keyframes zarfNefes {
            0% { transform: scale(1); }
            50% { transform: scale(1.08); }
            100% { transform: scale(1); }
        }
        .parsomon-kart {
            background: linear-gradient(135deg, #f4e8cb, #e3d0a8);
            color: #2b1d12;
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            width: 320px;
            margin: 0 auto;
            border: 3px solid #b8975f;
            text-align: center;
            font-family: 'Georgia', serif;
            animation: parsomonCikma 1s ease-out forwards;
        }
        @keyframes parsomonCikma {
            0% { transform: translateY(30px) scale(0.95); opacity: 0; }
            100% { transform: translateY(0) scale(1); opacity: 1; }
        }
        .parsomon-foto {
            max-width: 220px;
            width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.25);
            border: 3px solid #fff;
            margin-bottom: 15px;
            display: inline-block;
        }
        .parsomon-not {
            margin-top: 10px;
            padding-top: 15px;
            border-top: 1px dashed #9e7f4c;
            font-size: 14px;
            line-height: 1.6;
            text-align: left;
            color: #23170e;
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)

    if "zarf_acildi" not in st.session_state:
        st.session_state.zarf_acildi = False

    st.markdown('<div class="final-kutu">', unsafe_allow_html=True)

    if not st.session_state.zarf_acildi:
        st.markdown("""
            <div class="zarf-kutusu">
                <div class="zarf-ikon">💌</div>
                <h3 style="color: #4a2c11 !important; font-size: 20px; margin-bottom: 10px; font-family: 'Georgia', serif;">Sana Bir Mektup Var...</h3>
                <p style="color: #6e4722 !important; font-size: 13px; font-family: 'Georgia', serif;">Küçük Prens ve Tilki'den gelen özel sürprizi açmak için aşağıdaki butona dokun.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✨ Zarfı Aç"):
            st.session_state.zarf_acildi = True
            st.rerun()
    else:
        st.markdown(f"""
            <div class="parsomon-kart">
                {img_tag}
                <div class="parsomon-not">
                    <strong>İyi ki Doğdun Yavru Tilkim! 🦊🌹</strong><br><br>
                    <em>"Gözler kördür. İnsan ancak yüreğiyle baktığı zaman gerçeği görebilir. Hayatın boyunca kalbinin sesini dinlemen ve tüm güzellikleri bulman dileğiyle..."</em>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🔙 Başa Dön"):
            st.session_state.zarf_acildi = False
            st.session_state.asama = 1
            st.session_state.onay_adimi = 1
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
            
