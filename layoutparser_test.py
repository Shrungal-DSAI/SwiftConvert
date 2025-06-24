import layoutparser as lp
import cv2
import matplotlib.pyplot as plt

# Load the PDF page as image (first page only for now)
pdf_path = "C:/Users/Admin/Downloads/Antragsformular_0af903fb_4572_441b_8fcd_e4f19b222ae4.pdf"
image = lp.io.load_pdf(pdf_path, dpi=300)[0]  # First page

# Load EfficientDet layout model
model = lp.EfficientDetLayoutModel(
    config_path='lp://PubLayNet/efficientdet/efficientdet-lite3',
    label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"},
    extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5]
)

layout = model.detect(image)

# Visualize
lp.draw_box(image, layout, box_width=3).show()
