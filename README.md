# ACCOUNTING PROJECT

 RESTful API ile tasarlanmış bir muhasebe uygulaması
 Muhasebe ve işlemlerin tutulduğu temel CRUD işlemlerini yapabilen birim testlerini(CRUD) gerçekleştiren JWT (JSON Web Tokens) tabanlı yetkilendirme kullanılan,  
 Kullanıcıların bağlı olduğu gruba göre izinlerini kontrol ederek endpointleri çalıştıran bir uygulama
 
Uygulama, farklı kullanıcı rolleri ve yetkilendirme mekanizmalarına sahip 

# Kurulum Başlatma:
django pip install
django python manage.py starapp app_name 
pip install djangorestframework
pip install PyJWT
Swagger için : ---pip install drf-yasg

Oluşturduğumuz django projesi içinde settings.py dosyasında gerekli düzenlemeler yapılmalıdır.(REST_FRAMEWORK ve JWT_AUTH ve VERİTABANI ayarları düzenlenmeli)
Serializers.py dosyası oluştutulmalı. CustomVerifyJSONWebTokenSerializer classı eklenmelidir.
Postqresql kullanılmış ayarlar bu şekilde düzenlenmiştir. Kullanılan veritabanına göre düzenleme eklenmeli.


# API Görünümü  -  Kullanıcı Kontrol - Yetkilendirme.

Model dosyaları ve serileazers.py dosyası oluşturulduktan sonra settings.py dosyası düzenlendikten sonra

---python manage.py makemigrations
---python manage.py migrate

komutları çalıştırılmalıdır.
Djangonun sunduğu User tablosu ile admin arayüzü ile giriş yapılmalı. # http://localhost:8000/admin/
python manage.py createsuperuser
komutu ile superuser eklenmeli istenilen kullanıcı bilgileri verilmelidir.(Tam Yetkili ve tüm gruplarda ekli olmalı)
Admin paneli Users 3 grup bulunmaktadır: İşlemci Admin Muhasebeci
Muhasebeci Firmalar için işlem yapabilirken işlemlere yetkisi bulunamamktadır.
İşlemci işlemlerle ilgili yetkilere sahiptir.
Admin tüm yetkilere sahiptir.
Bu kullanıcı grupları proje dizini içersinde bulunan create_group.py dosyası ile kullanıcı izinleri ise accounting app içersinde create_groups_and_permissions.py dosyası içersinde verilmiştir.
Bu dosyaları çalıştırmak için:
İlgli proje dizinleri içersinde 
---- python create_group.py 
---  python create_groups_and_permissions.py
çalıştırılmalıdır.

Request için Postman tool kullanılmıştır.

Token alması için api-token-auth post methodu ile gönderilmelidir. ( Token bilgisi belirli süre sonra yenilenmelidir.)
Burda tam yetkili bir kullanıcı oluşturulmalı
Url Bilgisi: -- http://localhost:8000/accounting/api-token-auth/
Postman Body :
 
		{
			"username": "testuser",
			"password": "testpassword"
		}
JSON Formatta gönderilmelidir
Company modeli için
API Endpointleri:
		Url Bilgisi:---http://localhost:8000/accounting/api/firmalar/
		Listelmek için GET methodu 
		Eklemek için POST methodu
		Güncellemek için GET Methodu -- Url Bilgisi ---http://localhost:8000/accounting/api/firmalar/{id}/
		Okumak için GET Methodu -- Url Bilgisi ---http://localhost:8000/accounting/api/firmalar/{id}/
		Silmek için DELETE Methodu -- Url bilgisi --http://localhost:8000/accounting/api/firmalar/{id}/
		
şeklinde düzenlenmelidir.
Transaction modeli için
# API Endpointleri:
		Url Bilgisi:---http://localhost:8000/accounting/api/islemler/
		Listelmek için GET methodu 
		Eklemek için POST methodu
		Güncellemek için GET Methodu -- Url Bilgisi ---http://localhost:8000/accounting/api/islemler/{id}/
		Okumak için GET Methodu -- Url Bilgisi ---http://localhost:8000/accounting/api/islemler/{id}/
		Silmek için DELETE Methodu -- Url bilgisi --http://localhost:8000/accounting/api/islemler/{id}/
		
şeklinde düzenlenmelidir.

Header alanı
Key: Content-Type   Value : application/json
Key: Authorixation  Value : Bearer {Token} ---  (Alınan Token bilgisi)( Token bilgisi belirli süre sonra yenilenmelidir.)

düzenlenmelidir.
Company için
Body :
{
    "company_name": "TEST FİRMASI ",
    "tax_number": "1234567890",
    "company_code": 4,
    "address": "TEST UPDATE",
    "added_date": "2023-10-14",
    "report": "Firma Raporu (isteğe bağlı)"
}

Transaction için:
{
  "transaction_type": "test",
  "amount": "90",
  "date": "2023-10-14",
  "report": "repor",
  "company": 2,
  "user": 7
}	
Atılan isteğe uygun şekilde body içeriği json (isteğe bağlı) formatta düzenlenmlidir.		
		

 # Kullanıcı Rolleri:
Admin: Tüm yetkilere sahiptir. Firma hesaplarını oluşturabilir, düzenleyebilir
ve silebilir. Raporlara erişim sağlayabilir.
Muhasebeci: Firma hesaplarını görüntüleyebilir ve raporlara erişim
sağlayabilir.
İşlemci: Sadece kendi oluşturduğu işlemleri görebilir ve düzenleyebilir

TEST :

Birim testlerin çalışması için 
-- python manage.py test 
komutu ile çalıştırılmalıdır. ( Token bilgisi belirli süre sonra yenilenmelidir.)

