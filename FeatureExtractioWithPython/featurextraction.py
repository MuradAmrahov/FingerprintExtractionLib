import cv2
import fingerprint_feature_extractor
import fingerprint_enhancer

# Ağ qara şəklin oxunması
img = cv2.imread('C:/Users/user/Desktop/DB4_B/102_8.tif', 0)

# Şəklin səliqəyə salınması
enhanced_img = fingerprint_enhancer.enhance_Fingerprint(img)

# Extract the minutiae features from the enhanced image
FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(
    enhanced_img,
    spuriousMinutiaeThresh=10,
    invertImage=False,
    showResult=True,
    saveResult=True
)
