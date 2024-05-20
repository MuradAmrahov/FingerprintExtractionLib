Bu layihə `opencv`, `fingerprint_feature_extractor` və `fingerprint_enhancer` kitabxanalarından istifadə edərək barmaq izi görüntüsünün təkmilləşdirilməsi və xırdalıqların çıxarılması prosesini nümayiş etdirir.
**Layihədə əsas addımlar:**
  1. Barmaq izi görüntüsünü oxumaq.
  2. Xüsusiyyətlərin daha yaxşı çıxarılması üçün barmaq izi görüntüsünü təkmilləşdirmək.
  3. Təkmilləşdirilmiş görüntüdən xırdalıqları (silsilə sonluqları və bifurkasiyalar) çıxarmaq.
**Tələblər**
-Python 3.x
- `opencv-python`
- `fingerprint_feature_extractor`
- `fingerprint_enhancer'


**Görüntünün Oxunması:** Görüntü OpenCV-nin cv2.imread funksiyası ilə grayscale rejimində oxunur.

**Görüntünün Təkmilləşdirilməsi: **fingerprint_enhancer kitabxanasının enhance_Fingerprint funksiyası ilə barmaq izi görüntüsü təkmilləşdirilir.

**Xırdalıqların Çıxarılması:** fingerprint_feature_extractor kitabxanasının extract_minutiae_features funksiyası ilə təkmilləşdirilmiş görüntüdən minutia xüsusiyyətləri çıxarılır. spuriousMinutiaeThresh, invertImage, showResult və saveResult kimi parametrlər müəyyən edilir.
