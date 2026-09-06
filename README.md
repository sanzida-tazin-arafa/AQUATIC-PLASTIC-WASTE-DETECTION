# AQUATIC-PLASTIC-WASTE-DETECTION
ARCHITECTURAL MODIFICATION AND COMPARATIVE STUDY OF THE STATE-OF-THE-ART OBJECT DETECTION MODELS FOR AQUATIC PLASTIC WASTE DETECTION


Plastic pollution in aquatic environments is a growing ecological concern; automated, realtime monitoring offers a scalable way to detect and track waste before it spreads. This thesis
develops and evaluates a real-time object detection system for aquatic plastic waste
monitoring, using a custom 8-class dataset of 1,912 annotated images covering common
categories of aquatic debris, including bottle caps, bags, bottles, cups, and straws. The dataset
shows wide object-scale variation, with mean object footprint ranging from 1.7% to 51.9%
of image area across classes, alongside a distinct challenge posed by thin, elongated objects
such as plastic straws.
We follow a two-phase design. Phase One benchmarks four real-time detectors: YOLOv8n,
YOLO11n, YOLO26n, and RT-DETR-l. YOLO26n achieves the strongest accuracy-efficiency balance, reaching the highest mAP50-95 (0.7007) among the YOLO-family
detectors and narrowly surpassing RT-DETR-l (0.6983) while using roughly 13 times fewer
parameters and running over five times faster, and is selected as the baseline for Phase Two.
Phase Two investigates whether single-variable architectural modifications to the YOLO26n
neck can improve on this baseline: CBAM backbone attention, an all-points learnable
weighted feature fusion mechanism (WeightedConcat), and four controlled single-point
ablation variants.
None of these modifications beat the baseline. CBAM comes with the largest accuracy and
speed penalty; all-points weighted fusion comes closest to baseline accuracy but at the
greatest inference-speed cost; and the four single-point variants cluster tightly below both the
baseline and the all-points configuration, suggesting a shared confound rather than four
distinct architectural effects. Per-class analysis further reveals a severe, persistent weakness
in detecting the plastic_straw class across every configuration, including the baseline,
indicating a structural limitation in detecting thin, elongated small objects under IoU-based
matching.
This work contributes a benchmarked, efficiency-aware baseline, a reusable weighted-fusion
implementation, documented negative architectural results, and a clear direction for future
work on elongated small-object detection.
