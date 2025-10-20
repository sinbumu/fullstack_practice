# service.py
from __future__ import annotations
from typing import List, Dict, Any
import io

import bentoml
from PIL import Image


@bentoml.service
class YOLOService:
    def __init__(self) -> None:
        from ultralytics import YOLO
        self.model = YOLO("yolov5s.pt")

    @bentoml.api
    def detect(self, image: Image.Image) -> List[Dict[str, Any]]:
        """
        입력: 이미지 파일 (multipart/form-data 'image')
        출력: [ {class_id, class_name, confidence, bbox_xyxy}, ... ]
        """
        results = self.model(image)
        r0 = results[0]
        boxes = r0.boxes
        names = r0.names

        output: List[Dict[str, Any]] = []
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
            output.append(
                {
                    "class_id": cls_id,
                    "class_name": names.get(cls_id, str(cls_id)),
                    "confidence": round(conf, 4),
                    "bbox_xyxy": [x1, y1, x2, y2],
                }
            )
        return output

    @bentoml.api
    def detect_image(self, image: Image.Image) -> Image.Image:
        results = self.model(image)
        r0 = results[0]

        plotted = r0.plot()
        img = Image.fromarray(plotted[:, :, ::-1])
        return img
