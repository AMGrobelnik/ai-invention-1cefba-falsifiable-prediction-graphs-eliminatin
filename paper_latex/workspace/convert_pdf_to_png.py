#!/usr/bin/env python3
"""Convert every page of paper.pdf to PNG at 150 DPI using PyMuPDF."""
import fitz  # PyMuPDF
import os

input_path = "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.pdf"
output_dir = "/ai-inventor/aii_data/runs/run_hryee3iKb6FG/4_gen_paper_repo/_4_assemble_paper/paper/workspace/page_screenshots"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(input_path)
dpi = 150
zoom = dpi / 72.0  # 72 DPI is default

print(f"PDF has {len(doc)} pages")
for i, page in enumerate(doc):
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    out_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
    pix.save(out_path)
    print(f"  Page {i+1}: {pix.width}x{pix.height} -> {out_path}")

doc.close()
print(f"Done. {len(os.listdir(output_dir))} pages saved to {output_dir}")
