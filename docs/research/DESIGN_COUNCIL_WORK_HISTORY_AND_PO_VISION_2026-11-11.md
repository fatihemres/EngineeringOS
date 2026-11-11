# EngineeringOS’a Aktarım Adayı — Tasarım Ekibi Araştırmasının Geçmişi, Bulguları ve PO Vizyonu

**Tarih:** 11 Kasım 2026 (Türkiye saati)  
**Belge türü:** Tarihli araştırma/handoff kaydı; **işletim sözleşmesi, sistem tasarımı kararı veya uygulama izni değildir**.  
**Kaynak proje:** MyLibrary — Design Council deneyleri (E3 devam ederken alınmış kesit).  
**Hedef kullanım:** EngineeringOS ekibinin ileride bu araştırmaya erişip ne yapıldığını, ne öğrenildiğini, ne istendiğini ve neyin henüz açık olduğunu anlayabilmesi.  
**Yayın durumu:** Bu belge ayrı bir EngineeringOS belge dalı ve **Draft PR** üzerinden incelemeye sunulan bir **araştırma/handoff adayıdır**. EngineeringOS `main` dalına entegre edilmemiş, çalışma akışına veya otomasyona uygulanmamıştır.

> **OKUMA UYARISI:** Aşağıdaki kayıtlar dört ayrı türde ifade içerir: (1) PO'nun doğrudan dile getirdiği ihtiyaç ve tepkiler; (2) deney ajanlarının raporları; (3) kullanıcıdan alınan dosyaların bağımsız kaynak/kare incelemeleri; (4) sonraki adımlar için hipotezler. Bunları birbirine dönüştürmeyin. Özellikle "Council hazır" ≠ "PO beğendi" ≠ "gerçek ürün kabul edildi" ≠ "EngineeringOS özelliği çalışıyor".

## 1. Neden bu kayıt tutuluyor?

MyLibrary için başlayan UI/UX tasarım deneyleri, zamanla farklı projelerde kullanılabilecek bir **yaratıcı, eleştirel, kanıt temelli AI tasarım ekibi** fikrine dönüştü. Amaç geçmişi tek bir parlatılmış başarı hikâyesi olarak aktarmak değildir. Neden başarısız prototipler üretildiği, hangi geri bildirimlerin dönüm noktası olduğu, hangi sorunların hâlâ çözülmediği ve Product Owner'ın nihai beklentisi de korunmalıdır.

**PO'nun temel isteği:** Ürünün amacını anlattığında ekip yalnızca belirtilen ekran veya kusurları yerine getirmesin; kullanıcı deneyimini ve görsel kalitesini **bütün olarak** ele alsın, uygun becerileri/araçları keşfetsin, alternatifleri gerçek prototiplerle denesin, kendi fikirlerini sorgulasın ve kendisinin sürekli her hatayı tarif etmesini gerektirmeden tek olgun sonuç sunsun. PO ürün yönünü ve nihai kabulü elinde tutar; ekip yöntem ve tasarım çözümlerini yaratıcı biçimde araştırır.

Bu ihtiyaç başlangıçta *MyLibrary Collections* üzerinden test edildi, ancak **önerilen yöntem tek bir uygulamaya veya tek bir estetiğe bağlanmamalıdır**.

## 2. Projenin bağlamı ve değişmeyen sınırlar

MyLibrary, Windows-first / cross-platform hedefli, Tauri 2 + React/TypeScript + Rust + SQLite kullanan, local/offline-first kişisel kitaplık uygulamasıdır. Deneylerde gerçek kitaplık verisi kullanılmaması, Edition/Physical Copy ayrımının bozulmaması, silinme/birleştirme gibi ürün kararlarının ajanlara devredilmemesi önemliydi. Collections, gelecekte üretim izni alabilecek ayrı bir ürün keşfi konusudur; deney prototipleri üretim uygulaması değildir.

**Ayrımı koruyun:** Tasarımcılara **yaratıcı özgürlük** tanımak; veri güvenliğini, proje kararlarını, lisans haklarını, gerçek kişisel verinin korunmasını, ağ izinlerini veya GitHub yazma/entegrasyon yetkilerini serbest bırakmaz. PO'nun özel durumlarda açıkça tanımladığı ürün/marka/tasarım sınırları da sessizce aşılamaz. Bir sınırı daha iyi bir alternatifle değiştirmek isteyen ekip öneri sunabilir; kendiliğinden karar veremez.

## 3. Kronoloji — ne yapıldı, ne oldu?

| Sıra | Araştırma / deney | Gerçek çıktı ve öğrenim | Kanıt sınırı |
| --- | --- | --- | --- |
| 0 | İzole Codex CLI/ajan araştırması | Bağımsız katılımcı bağlamları ve kullanılabilir gerçek model çağrıları araştırıldı; 62/62 deterministik host testi geçişi, gerçek tasarım kalitesini göstermedi. İlk auth/kota engelleri ve altı bilinmeyen kökenli host referansı kaydedildi. | Altyapı testi ≠ görsel kabul; host kökeninin bir kısmı UNKNOWN. |
| 1 | Compact list B-X2, ilk gerçek A/B/C Council | Üç gerçek katılımcıyla metinsel ortak karar üretildi. 10 çağrı denemesi/9 yanıt raporlandı. | Gerçek itiraz/karşı kanıt ve yüksek kaliteli görsel inceleme yoktu. |
| 2 | Collections v002, semantik Council | Manual/Smart Collections, Edition/Copy üyeliği, belirsiz Wishlist politikası, seri önerileri ele alındı. A/B/C birbirlerinin bazı önerilerini karşı örneklerle değiştirdi; 18 deneme/17 yanıt raporlandı. | Metinsel uzlaşı, ayrı üretilen HTML mockup'ın görsel kabulü değildi; ilk arayüz jenerik kaldı. |
| 3 | *The Reading Table* v3, ortak tasarım stüdyosu | Üç katılımcı renderları eleştirip ilk sürümü reddetti; daha sıcak, editoryal bir kitaplık görsel dili üretti. 21 çağrı raporlandı. PO büyük ilerleme gördü, fakat genel beğenisi yaklaşık 6–7/10 idi. | Modal, Description ve Grid/List geçişleri aniydi; küçük tipografi ve standart kontroller kaldı. Üretim onayı verilmedi. |
| 4 | E1, eşit yaratıcı yetki | A/B/C aynı bitmiş tasarımı görüp karşılıklı eleştirdi. Description ara kareli genişleme aldı; Grid/List öğeleri taşındı. 16/24 çağrı, 530.933 giriş/39.228 çıkış token raporlandı. | Hareket gerçekti ancak kitap yolları ve içerik birbirine giriyordu. ZIP kaynak/hareket kareleri ayrıca incelendi. |
| 5 | PO'nun gerçek ekran videosu | “Çötenk” tanımı somutlaştı: Grid/List seçici ve içeriği farklı biçimde anlık değişiyor, modal ve sayfa geçişleri mekânsal bağ kurmuyordu. PO basma/hover gibi iyi mikrodavranışları korumak istedi. | Kullanıcının doğrudan algısal geri bildirimi; tüm native/platform testleri değil. |
| 6 | E1-R2 v4, motion rafinasyonu | Ekip gerçek karelerde çakışmaları görüp hareket fikirlerini değiştirdi; modal metin ghosting giderildi, Grid/List aktif göstergesi yaklaşık 150 ms kaymaya başladı. 20/20 çağrı raporlandı; 641 dosya ve 486 kare bağımsız hash kontrolünden geçti. | Çakışma azaltıldı ama kitapların yerleşimi/sayfa içeriği hâlâ büyük ölçüde bir anda değişiyordu. |
| 7 | E2, dördüncü motion-perspektifli D | D için ilk iki çağrı NETWORK hatası verdi; sonraki canary başarılı oldu. Toplam 19/20 deneme, 17 yanıt. Dördü tek adayı inceledi; 133 prototip, 5 oynatıcı, 8 teslim kontrolü *ajan tarafından* raporlandı. Bütünsel UX iyileşmeleri ve daha kompakt düzen sağlandı. | Bağımsız ZIP/kaynak incelemesi, JS yapısal hareketlerinin bilerek kapatıldığını gösterdi: `const canAnimate = () => false`. v4'teki kayar gösterge de geriledi. PO yine “çötenk” dedi. D ayrı promptlanmış model bağlamıydı; doğrulanmış ayrı motion skill'i değildi. |
| 8 | E3 Motion Craft Lab, **devam ediyor** | Amaç gerçek normal hızlı WebM hareketi, birbirinden farklı geçiş prototipleri ve bütünsel keşif. Ekran görüntüsüne göre 4/16 Council çağrısı/4 bağımsız keşif raporlandı. | Kota/otomatik onay değerlendirmesi `You've hit your usage limit` yüzünden durdu. **E3 final, kalite başarısı ve PO kabulü henüz yok.** |

**Önemli düzeltme:** Deneylerin gerçek cihaz, native WebView2/DPI/FPS, ekran okuyucu ve erişilebilirlik kabulü büyük ölçüde yapılmadı. Ajanların PASS/READY demesi bu koşulları yerine getirmez. Eski deneylerin zamanlamaları, çağrı sayıları ve bazı araç/kimlik iddiaları çoğu durumda **Codex raporudur**; bunların kendiliğinden bağımsız doğrulanmış bilgi olduğu varsayılmamalıdır.

## 4. Özellikle saklanması gereken başarısızlık ve karşı örnekler

1. **Metinsel uzlaşı iyi UI demek değildir.** v002'nin doğru görünen semantik kararlarından jenerik bir arayüz çıktı; gerçek görseli bütün uzmanlar değerlendirmemişti.
2. **Tek üretici + üç isim bağımsız görsel tasarım demek değildir.** Aynı renderları tüm katılımcıların görüp değerlendirmesi kaliteyi iyileştirdi.
3. **“Animasyon kodda var” iyi motion demek değildir.** İlk E1'de ara kareler ve kaydırmalar vardı, ama öğeler çatallandı; kısa modal animasyonları PO'ya hâlâ ani geldi.
4. **Çakışmayı hareketi kapatarak çözmek özgün hedefi karşılamaz.** E2'nin `canAnimate() => false` kararı bunun en somut anti-pattern'idir. Güvenli reduced-motion/fallback ayrı bir ihtiyaçtır; sıradan kullanımda algısal hedef karşılanmadığında PASS verilmemelidir.
5. **Daha fazla “uzman” daha iyi tasarımı garanti etmez.** D ayrı model bağlamıyla motion fikri getirdi, ancak kendi önerilerini geri çekti ve sonuçta hareket kalitesi ilerlemedi. Kalıcı uzmanlık veya üstünlük kanıtlanmadı.
6. **Seçilmiş JPEG kareleri gerçek zamanlı hissi eksik temsil eder.** Birden fazla dizide zaman sırası kusurları vardı; WebM ve doğrudan normal hızda izleme ayrı bir kalite kanıtıdır. Video kaydı da tek başına FPS ölçümü veya insan kabulü değildir.
7. **Başarılı otomatik testler estetik kabulü kanıtlamaz.** 48/48, 133/133 veya hash PASS yalnızca ilgili testlerin kapsamını doğrular. Görsel kalite ve kullanıcı tercihleri ayrı değerlendirilmelidir.
8. **Sadece PO'nun işaret ettiği alanları düzeltmek bütünsel sahiplik değildir.** PO, ekibin kendi kendine bütün ekranları, durumları ve akışları eleştirmesini istedi.
9. **Tartışmayı uzatmak kaliteyi otomatik artırmaz.** Yüksek model çağrı/token maliyeti nedeniyle hedefli kanıt paketleri ve anlamlı durdurma noktaları araştırılmalıdır.
10. **Katılımcı bağlantısı ve kota hataları tasarım sonucu değildir.** Ağ/kota yüzünden yanıt gelmediğinde yanlış konsensüs üretilmemeli; başarısız denemeler korunmalıdır.

## 5. Product Owner ne istiyor? — ifadeye en yakın hedef kaydı

Aşağıdakiler uygulanmış sistem özellikleri değil, **PO'nun sohbet boyunca geliştirdiği hedef ve tercihlerin kaydıdır**.

### 5.1 Ürün vizyonuyla başlama

PO, yeni bir uygulamada “kitaplık uygulaması yapıyoruz; kitap kaydedilecek, kitaplık gösterilecek” gibi **ne yapılmak istendiğini** anlatmak istiyor. Ekip yalnızca literal ekran listesiyle yetinmemeli; kullanıcıları, iş akışlarını, boş/hata/dar pencere durumlarını, uygun teknik/tasarım seçeneklerini araştırıp kendi önerilerini geliştirmeli. Bununla birlikte Edition/Copy, gizlilik, veri güvenliği ve somut ürün kapsamı gibi kabul edilmiş kararları kendiliğinden değiştirmemeli.

### 5.2 Yaratıcı özgürlük varsayılan; istisnalar bağlama bağlı

PO, **çoğu durumda ekibin başlangıçta beğenilen tasarım yönünü bile aşabilecek özgürlüğe sahip olmasını** tercih ediyor. Sınırlar nadiren ve açıkça belirtilen bağlama göre olabilir. Öneriler sunabilir ve daha iyi alternatifleri kanıtlayabilirler; kesin PO kararlarını sessizce değiştiremezler.

**Kısa ilke adayı:** “Creative Freedom by Default / Challenge the Direction, Respect the Decision.” Bu slogan **konuşmadaki üzerinde uzlaşılan yönü özetler**, henüz EngineeringOS'ta çalışan kural veya kabul edilmiş repo politikası değildir.

### 5.3 Eşit yaratıcı katkı, tamamlayıcı bilgi

A/B/C/D tüm görsel tasarım, yerleşim, kullanılabilirlik, motion, erişilebilirlik ve etkileşim konularında fikir üretebilir, eleştirebilir ve fikir değiştirebilir. Uzmanlığı bir konuya **münhasır oy hakkı veya veto** yapmamak önemlidir. Ama teknik kaynak doğrulaması ve bağımsız inceleme ayrıca üreten aktörden farklı bir inceleyici gerektirebilir.

### 5.4 Gerçek tartışma, sonra tek final

Birbirinden kopuk birkaç tamamlanmış tasarımı sürekli PO'ya getirmek istenmiyor. Ekip içeride farklı konseptler üretebilir, kıyaslayabilir, eleştirip geri çekebilir, gerçek prototipler deneyebilir; sonra **tek ortak olgun aday** sunar. Anlamlı uyuşmazlıklar, çözülmeyen riskler ve neden bir tercih yapıldığı kayıtlı olmalıdır. Hiçbir fikrin sorgulanmadan uygulanması da, zorla konsensüs oluşturulması da istenmiyor.

### 5.5 Başlangıçta hafif PO görsel/motion yön kalibrasyonu

Yeni ürün/önemli yeniden tasarımda, yüksek maliyetli büyük prototipe başlamadan önce **küçük, farklı görsel yönler ve kısa gerçek motion örnekleri** gösterilebilir. PO birini tek parça seçmek zorunda değildir; A'nın atmosferini, B'nin kullanım düzenini, C'nin hareket hissini beğenebilir. Ekip bu beğeninin *nedenini* anlar, ilk mockup'a hapsolmadan daha iyi alternatif üretir.

Bu adım **her küçük UI görevi için tekrarlanmaz**: zaten kabul edilmiş tasarım yönü varsa kullanılır; açık yeni yön/çelişki yoksa PO'dan yeniden oy istenmez. Erken örneklerin yaratıcılığı sabitleme (*design fixation*) riski unutulmamalıdır.

### 5.6 Kapsamlı kalite, sadece “istenen düzeltme” değil

Ekip yalnızca PO'nun söylediği “Grid/List”, “modal” veya “description” sorununa bakmamalı. Tam kullanıcı yolculuğu, butonlar, kitap kapakları, tipografi, arama/filtreler, hata durumları, klavye, odak, EN/TR, açık/koyu tema, dar ekran, performans ve uygun hareket dili **bütün olarak** ele alınmalıdır. Bir noktada iyi davranış tespit edildiyse sadece yenilik uğruna bozulmamalıdır.

### 5.7 Araç/beceri ağı, ama zorunlu “hepsini kullan” değil

PO, Motion, GSAP, LottieFiles, Rive, Impeccable, Taste, UI UX Pro Max ve başka kaynakları araştırıp ekibin kaçırdığı hiçbir önemli yetenek olmamasını merak ediyor. **Geniş araç keşfi, hepsinin aynı anda kurulması değildir.** İşe uygun, güvenli, lisans ve ortam açısından doğrulanmış yetenekleri seçmek; uyumsuz kütüphaneleri yığmamak fikri tartışıldı. Her kurulum, dış servis, ağ ve depoya kod yazımı ayrıca kapsamlı izin gerektirir.

### 5.8 EngineeringOS ile gelecekte kendiliğinden doğru zamanda buluşma

PO'nun yeni sorusu: Codex ilk kitap kayıt/kitaplık ekranını geliştirirken **Design Council nasıl ve ne zaman devreye girer?** İstenen yön, tek bir prompta yüzlerce kural yazmak değil; EngineeringOS'un görevi sınıflandırıp uygun uzmanlık/kalibrasyon/inceleme ihtiyacını unutmaması. İlk kez UI kurulurken erken tasarım desteği; küçük düzeltmelerde kabul edilmiş Design Direction Brief'in yeniden kullanılması; veri/migration işlerindeyse yalnızca UX etkisi varsa tasarım desteği gibi **bağlama duyarlı yönlendirme** araştırılıyor.

Şimdiki EngineeringOS Foundation'da **çalışan otomatik agent-router, multi-agent runtime veya sürekli proje senkronizasyonu yoktur**. Gelecekteki olası “Design Task Router + Design Direction Brief + UI Quality Gate” bileşenleri yalnızca öneridir, mimari/roadmap/uygulama kararı değildir.

## 6. Fikirler ve araştırma adayları — durum açık

| Fikir / aday | Neden gündeme geldi? | Şimdiki statü |
| --- | --- | --- |
| Genel amaçlı tasarım ekibi, henüz isim yok | Üç Silahşörler/Athos-Porthos-Aramis ve D'Artagnan esprisinden ürüne özel olmayan isim arayışı doğdu | **İsim seçilmedi**; karakter eşlemeleri kalıcı rol değil |
| Kalibrasyon protokolü | Büyük tasarım harcamasından önce PO'nun beklentisini anlamak | **Yöntem önerisi**; oluşturulmuş metin başka dosyada, EngineeringOS'a entegre değil |
| “Creative Freedom by Default” | Kişinin niyetini korurken kısıtlamamayı tercih etmesi | **PO yönü**; repo-standardı/runtime olarak uygulanmadı |
| Bütünsel tasarım sorumluluğu | Yalnızca bildirilen kusurları düzeltme sorunu | **PO beklentisi**; başarı deneysel olarak değerlendirilmeli |
| Gerçek motion uzmanlık/skill takviyesi | D ayrı bir prompttu; E2'de hareket gelişmedi | **Aday araştırma**; kalıcı üye veya skill kabul edilmedi |
| Motion / GSAP Flip / WAAPI / Rive / Lottie | Algısal geçiş sürekliliği ve özel animasyon için farklı araçlar | **Karşılaştırma adayları**; beraber kurulum/adoption yok |
| İki katmanlı bağımsız kalite incelemesi | Ekip kendi çıktısını beğendiğinde hataları göremeyebilir | **Yöntem hipotezi**; bağımsız aktör ve sesli/video kanıtı gerekli |
| Greenfield baştan tasarım | Mevcut prototip etrafındaki tasarım sabitlenmesi | **Merak/deney fikri**; ürün kapsamına izin değil |
| Otomatik/smart task router | Codex özellik geliştirmeye başlarken tasarım ihtiyacını kaçırmasın | **Mimari fikir**; EngineeringOS'ta runtime mevcut değil |
| Ürünler arası deneyim aktarımı | MyLibrary'den edinilen dersler diğer uygulamalara taşınsın | **Özel çalışma alanı / gözden geçirilmiş Public Core ayrımı**; otomatik senkronizasyon yok |

## 7. Neler kesinleşmedi, neye “uygulanıyor” denmemeli?

- Design Council / dört silahşörün **kalıcı üye sayısı, rolleri veya adı** seçilmedi.
- Hiçbir görsel tema, UI bileşen seti, motion kütüphanesi veya otomatik skill kurulumu **üretim için kabul edilmedi**.
- Greenfield tam tasarım veya E3 sonucu henüz **PO tarafından kabul edilmedi**.
- EngineeringOS `main` içinde tasarım yönlendiricisi veya kalibrasyon otomasyonu **çalışmıyor**.
- Üç/dört aktörün “READY” raporu, bağımsız kod/görsel değerlendirme veya Windows yerel kabulün yerine geçmez.
- Tasarım ekibinin PO'dan bağımsız ürün özelliği, kapsam, entegrasyon, release, veri şeması veya özel servis kararı alma yetkisi yok.
- İlk görsel kalibrasyonun ne sıklıkta yapılması gerektiği, kullanıcı sayısı, bütçe ve örnek sayısı **konuşulmuş ama ölçülmüş değil**.
- EngineeringOS'a ham sohbet, kişisel veri, kullanıcı profil dosyaları, deney ZIP'leri, kimlik bilgileri veya oturum/log kopyası **gönderilmedi**.

## 8. EngineeringOS bu kaydı ileride nasıl değerlendirebilir? — talimat değil, aktarım amacı

Gelecekteki EngineeringOS çalışmasında bu belge, **geçmiş/niyet/fikir girdisi** olarak okunabilir. İlgili ekip, mevcut kabul edilmiş repo/proje sözleşmeleri ile karşılaştırıp çelişkileri belirler; tasarım ilkeleri, beceri seçimi, orkestrasyon yönlendirmesi ve kalite kanıtı gibi konularda öneri üretebilir. Bu fikirlerin **hangisinin EngineeringOS kalıcı sözleşmesi olacağı** ve ne zaman uygulama izni verileceği ayrıca PO kararına bağlıdır.

Kullanılabilecek kavramsal bilgi hattı:

`İş geçmişi ve PO beklentisi → kanıt/eksiklerin değerlendirilmesi → mimari/iş akışı önerisi → ayrı PO kararı → gerekiyorsa kontrollü uygulama ve doğrulama → kayıt güncellemesi`

**Bu belge, “her görevde X ajanını otomatik çağır”, “tüm kütüphaneleri kur”, “tasarım yönünü her seferinde yeniden oylat” veya “kalıcı sözleşme budur” şeklinde yorumlanmamalıdır.**

## 9. Kaynaklar ve izlenebilirlik

- **Birincil kronoloji:** [MyLibrary — Design Council Evidence Ledger & EngineeringOS Transfer Pack, Draft PR #59](https://github.com/fatihemres/MyLibrary/pull/59), dal `docs/design-council-evidence-ledger-20261110`, dosya `docs/development/devex/DESIGN_COUNCIL_EVIDENCE_AND_ENGINEERINGOS_HANDOFF.md`. Son bu kesitte canlı doğrulanan aday HEAD: `5c3a2ba8b7f548efa6917690dccd6ae457c60a6c` (**Draft / unmerged**).
- **MyLibrary korunmuş aktif dalı:** `v2` SHA `10510ab0c5a5d413717cf736b1d74d3590b39e2b` (2026-11-11 canlı doğrulama). Prototiplerin hiçbiri bu dala entegre edilmiş üretim ürünü değil.
- **EngineeringOS Public Core:** [EngineeringOS repository](https://github.com/fatihemres/EngineeringOS), `main` SHA `2f31e248bf82f64870bb9591aafdfc53261add19` (2026-11-11 canlı doğrulama). O an Foundation `v0.1` entegre, orkestrasyon runtime'ı henüz uygulanmamış.
- **EngineeringOS kaynak sözleşmeleri:** `AGENTS.md`, `ARCHITECTURE.md`, `docs/ORCHESTRATION.md`, `workflows/ui-ux-craft.md`, `docs/CAPABILITY_NETWORK.md`, `docs/P0_CAPABILITY_CONTRACT_DISCOVERY.md`, `docs/MEMORY.md`, `docs/PRIVACY.md`, `docs/DECISIONS.md`.
- **Ayrı hazırlanmış, kabul edilmemiş gelecek-protokol önerisi:** `ENGINEERINGOS_DESIGN_DIRECTION_CALIBRATION_PROTOCOL_PROPOSAL_2026-11-11.md` (yerel oluşturulmuş dosya; bu belgenin kendisi veya EngineeringOS kaydı değildir).
- **Deney artefaktları:** Kullanıcının özel araştırma klasörlerinde saklanan v3, E1, E1-R2, E2, E3 kaynakları/prototipleri, hareket kayıtları, bağımsız raporlar. Bu aktarımda yalnızca **kimlik ve ilişki** belirtilir; ham dosyaların otomatik paylaşımı yoktur. Kesin kaynağa erişim ve yayın hakkı ayrı doğrulanmalıdır.

## 10. Sonraki sohbet için kısa başlangıç notu

Bu çalışma, MyLibrary'yi baştan tasarlayıp kabul ettirme kararı değildir. PO, yerel/izole denemelerde çok uzmanlı tasarım işbirliği modelini sınadı. Takımın fikir değiştirme kabiliyeti gelişti; hareketin algısal kalitesi ise teknik PASS'a rağmen sıklıkla yetersiz kaldı. Dördüncü motion perspektifi tek başına sorunu çözmedi. E3, gerçek video ve hareket deneyiyle bunu düzeltmeye çalışırken henüz tamamlanmadı.

PO'nun hedefi, EngineeringOS'a taşınabilir; ürün vizyonundan başlayabilen, gerektiğinde başlangıçta kısa PO yön kalibrasyonu yapan, **yaratıcılığı varsayılan olarak özgür bırakan**, tüm UI/UX'u sahiplenen, araçları göreve göre seçen, alternatifleri karşılaştıran, tek ortak tasarım sunan ve gerçek hareket/erişilebilirlik/bağımsız kalite kanıtı üreten bir tasarım çalışma kültürüdür. Geliştirme sırasında Codex'in tasarım desteğini ne zaman çağıracağını anlama fikri de araştırılmaktadır. Bunlar **PO vizyonu ve aday mimari fikirleridir**; uygulanmış otomasyon veya kalıcı EngineeringOS kuralları değildir.

Bu kayıt orijinal kanıtların yerine geçmez. Yeni bir araştırmada önce güncel repo durumu ve değişmiş PO kararları kontrol edilmeli; eksik deney kaynakları, izinler, maliyet ve görsel kabul ayrı kaydedilmelidir. Bu araştırma kaydının ayrı belge dalında commit/push edilmesi ve Draft PR açılması **2026-11-11 tarihli kapsamla sınırlı PO iznine** dayanır. İlerideki ek repo değişiklikleri, EngineeringOS çalışma protokollerinin kabulü, `main` entegrasyonu ve release/yayın için **ayrı açık PO izni** gerekir.