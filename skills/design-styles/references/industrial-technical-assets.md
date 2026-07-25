# Industrial & Technical Images & Graphic Assets Guide 2026

> Comprehensive, brand-neutral art direction for photography, technical illustration, icons, pictograms, borders, separators, diagrams, charts, maps, video, 3D, and visual evidence.


## 1. Purpose

Industrial visual assets must make complex products, processes, environments, and capabilities easier to identify, verify, compare, and understand. A technically styled asset that communicates no useful information is decoration.


## 2. Asset hierarchy

Classify assets as evidence, explanation, navigation, or atmosphere.

Evidence includes real facilities, products, processes, installations, people, projects, tests, and certificates. Explanation includes drawings, diagrams, exploded views, charts, maps, annotated images, simulations, and 3D models. Navigation includes icons, pictograms, status symbols, arrows, and category markers. Atmosphere includes grids, material textures, background video, and abstract geometry.

```text
Evidence > explanation > navigation > atmosphere
```


## 3. Visual direction

Appropriate directions include documentary industrial, technical precision, engineered editorial, material and process, infrastructure scale, operational human, product-led, and data-led.

Select one primary direction. Do not mix generic cyberpunk, blueprint texture, glossy SaaS graphics, hazard motifs, and random construction photography without a coherent system.


## 4. Photography strategy

A complete production should include facility exterior, operational overview, medium process, product in use, material detail, real people working, inspection, finished output, scale reference, and role-based portraits.

Build a reusable evidence library rather than a set of unrelated hero images.


## 5. Documentary accuracy and safety

Use real locations, real activity, correct equipment, credible sequencing, and restrained staging. Before publication verify PPE, machine guards, lifting practices, exclusion zones, vehicle routes, isolation, chemical handling, working at height, signage, and housekeeping.

An attractive image can damage credibility if it documents unsafe practice. Do not digitally add or remove PPE without qualified review.


## 6. Product photography

Create front, side, rear, top, connection detail, scale, included components, installed context, packaging, and identification-plate views where relevant.

Preserve true color, material, finish, configuration, proportions, and included parts. Caption the exact model and configuration. Do not combine product generations without explanation.


## 7. Process, facilities, and people

Process imagery should show input, preparation, operation, inspection, and output. Facilities imagery should establish location, production floor, test area, storage, loading, scale, and working context. Drone imagery may establish scale but should not replace ground-level proof.

Show people performing credible tasks such as operating, measuring, inspecting, maintaining, planning, and training. Avoid staged pointing, fake meetings, and invented employee or diversity claims.


## 8. Composition and grading

Define camera height, focal length, perspective, negative space, crop direction, lighting, and staging. Strong industrial composition often uses structural lines, repetition, material contrast, process layers, and human scale.

Preferred grading preserves accurate material color, realistic skin, neutral balance, and shadow detail. Avoid universal teal-orange grading or excessive HDR.


## 9. Ratios, crops, captions, and alt text

Use a limited ratio system, for example:

```text
Hero: 16:9 or 2:1
Feature: 3:2
Process: 4:3
Product: 1:1 or 4:3
Portrait: 4:5
Detail: 1:1
```

Prepare mobile crops that preserve identifiers, faces, and operating context.

Captions should identify subject, product/model, process, location, date, and configuration where relevant. Alternative text should describe the useful technical content, not merely say “industrial image.”


## 10. Technical illustration

Use technical illustration for internal structure, parts, assembly, dimensions, flow, inaccessible views, installation, maintenance, and comparison.

Define projection, line weights, hidden lines, sections, dimensions, numbering, callouts, color coding, scale, and revision. Do not imitate engineering drawings inaccurately.


## 11. Exploded and annotated views

Exploded views should communicate part relationship, assembly order, identification, orientation, and optional components. Use consistent separation, numbered parts, a part list, and minimal crossing callouts.

Annotated photography may identify components, inspection points, flow, damage, dimensions, or installation. Preserve an unannotated source, use consistent callouts, and provide a nonvisual text list.


## 12. CAD, BIM, drawings, 3D, and simulation

Drawing previews should show title, model, revision, drawing number, date, and file type. A raster preview is not the authoritative drawing.

3D may support rotation, configuration, assembly, internal views, and installation. Provide a fast static fallback, labelled controls, reset, loading state, keyboard access, reduced motion, and mobile performance.

Clearly label live data, simulation, example data, forecast, design model, and operational model. Never present simulation as measured performance.


## 13. Icons and pictograms

Define one base grid, stroke, fill, corner, optical size, and status system. Categories may include products, applications, services, documents, materials, tools, transport, utilities, and support.

Use text labels for unfamiliar symbols. Official safety and regulatory symbols must use approved sources and must not be redrawn casually or used decoratively. Custom pictograms must not resemble official hazard marks with a different meaning.


## 14. Borders, separators, arrows, and connectors

Suitable borders include technical panel edges, drawing frames, measurement corners, indexed rules, accent edges, and image frames.

Separators may be full rules, inset rules, dashed process lines, indexed dividers, coordinate labels, material transitions, or whitespace. Dashed lines need a defined meaning.

Define different visual semantics for material flow, data flow, user process, mechanical motion, and optional relationships. Do not use one arrow style for every meaning in a complex system.


## 15. Process and architecture diagrams

Process diagrams should identify start, steps, decisions, output, owner, and exceptions. Create a simple overview and an optional detailed version.

Architecture diagrams should distinguish hardware, software, users, external services, databases, sensors, and control systems. Show direction, system boundaries, trust zones, protocols where relevant, and provide a responsive text equivalent.


## 16. Charts and performance curves

Use charts for genuine questions such as capacity, pressure drop, temperature range, reliability, lifecycle, emissions, lead time, response, or test results.

Include units, conditions, source, date, model, test standard, actual versus estimate, uncertainty, operating range, and prohibited regions where relevant. Use honest axes and provide a data table.

A performance curve must not be simplified until engineering meaning is lost.


## 17. Maps, certifications, and document graphics

Use maps only where geography matters: facilities, routes, coverage, projects, distribution, or installed base. Provide labels and a location list.

Use official customer and certification assets with permission, correct version, clear space, and scope. Do not imply that an organization-level certification applies to every product.

Document thumbnails may use type icons, revision badges, language, file size, and status, but the document title must remain live text.


## 18. Patterns and texture

Appropriate patterns include technical grids, measurement ticks, line hatching, dot fields, map contours, and restrained blueprint references. Material macro photography may provide texture.

Keep pattern and texture subordinate, avoid text interference, tie scale to the layout, use SVG/CSS where possible, and do not turn compression artifacts into a style.


## 19. Video and motion

Use video for process, machinery, installation, product behavior, training, facility scale, or expert explanation.

Provide captions, transcripts for important content, a poster image, pause controls, no autoplay audio, chapter markers for long technical content, model/configuration context, and revision dates for training.

Motion should explain sequence or behavior, not delay specifications.


## 20. AI-generated imagery

AI-generated imagery may be appropriate for clearly conceptual illustration, campaign backgrounds, early visualization, or generic explanatory scenes.

It must not serve as evidence of a real facility, employee, customer, project, product performance, certification, or safe work practice. Record generation provenance and require domain review.


## 21. Responsive delivery and formats

Use `<picture>`, `srcset`, and `sizes`; prepare mobile crops; provide intrinsic dimensions; prioritize the hero; lazy-load below-fold assets; use AVIF/WebP for photography and SVG for line graphics; progressively load 3D; and never ship a full-resolution drawing as a page image.

Name files descriptively, for example:

```text
hero-offshore-valve-installation-wide.avif
product-vx400-front-01.webp
process-pressure-test-03.webp
diagram-vx400-flow-path.svg
drawing-vx400-dimensions-r04.webp
icon-service-calibration.svg
```


## 22. Rights and provenance

Store creator, date, location, subject, product, configuration, license, consent, revision, source, modifications, and approved usage. This is essential when assets support technical, safety, compliance, or legal claims.


## 23. AI prompt template

```text
Documentary industrial photograph for [sector].
Subject: [specific product/process/person].
Activity: [credible task].
Environment: [facility or operating context].
Safety: [correct PPE and safe practice].
Lighting: [natural or controlled].
Composition: [wide/medium/detail and negative space].
Color: accurate industrial materials.
Page role: [hero/case/product].
Exclude: fake holograms, unsafe behavior, invented logos, illegible text,
incorrect equipment, exaggerated cinematic effects.
Aspect ratio: [ratio].
```

Generated results require review by someone with relevant domain knowledge.


## 24. Anti-patterns

Avoid generic factory stock, fake holograms, unsafe work, incorrect machinery, impossible configurations, decorative safety colors, fake charts, misleading performance curves, inaccessible diagrams, tiny text in images, generated facilities presented as real, mixed icon families, random dashed lines, excessive blueprint texture, unoptimized 3D, irrelevant drone footage, and unauthorized customer marks.


## 25. AI-agent rules

The agent must classify each asset, determine factual risk, define exact subject and configuration, plan image series and crops, define icon and pictogram rules, define drawing and diagram language, specify chart requirements, create captions and metadata, provide accessible equivalents, optimize formats, record provenance, distinguish generated from documentary, and require expert review for safety or technical claims.


## 26. Production checklist

### Photography
- [ ] Correct equipment and configuration
- [ ] Correct PPE and safe practice
- [ ] Real process and context
- [ ] Wide, medium, and detail
- [ ] Desktop and mobile crops
- [ ] Captions, rights, and consent

### Technical graphics
- [ ] Projection, line, dimension, and revision rules
- [ ] Callouts and numbering
- [ ] Units and conditions
- [ ] Accessible explanation
- [ ] Mobile alternative

### Graphic system
- [ ] Icon grid and stroke
- [ ] Approved pictograms
- [ ] Border and separator meanings
- [ ] Arrow and flow semantics
- [ ] Chart and map rules

### Delivery
- [ ] Responsive formats
- [ ] Intrinsic dimensions
- [ ] SVG optimization
- [ ] 3D fallback
- [ ] File-size review
- [ ] Provenance stored


## 27. Research basis

- DBS Interactive, 2026 Trends for Manufacturing Website Design: https://www.dbswebsite.com/blog/manufacturing-website-design-trends/
- Valmax, Best Manufacturing Websites of 2026: https://valmax.agency/insights/best-manufacturing-websites-of-2026/
- Windmill Strategy, B2B Web Design Trends 2026: https://www.windmillstrategy.com/top-9-b2b-web-design-trends/
- W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C, Images of Text: https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html
- web.dev, Responsive Images: https://web.dev/articles/responsive-images
- web.dev, Image Performance: https://web.dev/learn/performance/image-performance

---

## Final rule

Industrial visual assets must prove, explain, identify, or guide. A dramatic asset is not useful if it misrepresents the product, process, safety context, or technical result.

---

# Research Basis v2 — Visual Evidence, Accessibility, and Asset Governance

## A. Research methodology

The visual-asset rules combine:

1. WCAG requirements for non-text content, images of text, use of color, and graphical contrast.
2. Product-page and specification-heavy B2B usability research.
3. Performance guidance for responsive images.
4. Sector-specific requirements for technical accuracy, safety, revisions, and provenance.

## B. Source-to-rule mapping

### B.1 Product imagery supports evaluation

Baymard product-page research supports using sufficiently detailed imagery and descriptions to answer evaluation questions.

**Rules:**

- Create front, side, detail, scale, configuration, installed-context, and identification views when relevant.
- Pair imagery with model and configuration text.
- Do not use one atmospheric hero image as the complete product visual record.
- Keep product-list thumbnails informative enough to support preliminary comparison.
- Maintain accurate color, material, included components, and scale.

### B.2 Accessible non-text content

WCAG requires equivalent alternatives for meaningful non-text content.

**Rules:**

- Informative diagrams need alt text.
- Complex technical graphics need detailed adjacent descriptions.
- Chart values require a table or structured equivalent where important.
- Decorative textures and grids should be hidden from assistive technology.
- Functional icon buttons require accessible names.

### B.3 Text inside images

WCAG recommends real text instead of images of text when the visual presentation can be achieved with web technologies.

**Rules:**

- Keep product names, values, units, warnings, drawing titles, document revisions, and CTA labels outside raster images.
- Preserve image-only text only when it is part of a photographed object, official mark, or essential technical source.
- Provide transcription for meaningful photographed labels or archive documents.

### B.4 Non-text contrast and color

**Rules:**

- Callout lines, diagram nodes, input boundaries, chart series, and functional icons need sufficient contrast.
- Color-coded systems need labels, symbols, patterns, or direct annotation.
- Official hazard and regulatory colors and symbols must retain their approved meaning.

### B.5 Responsive image performance

web.dev identifies image optimization as central to web performance.

**Rules:**

- Generate width variants.
- Use AVIF/WebP for photography.
- Use SVG for appropriate line art.
- Define dimensions to avoid layout shift.
- Use art-directed mobile crops.
- Lazy-load noncritical galleries and drawings.
- Use static fallbacks for 3D and video.

## C. Expanded authoritative source set

### Accessibility and standards

- W3C, WCAG 2.2  
  https://www.w3.org/TR/WCAG22/
- W3C, Understanding Non-text Content  
  https://www.w3.org/WAI/WCAG22/Understanding/non-text-content
- W3C, Images Tutorial  
  https://www.w3.org/WAI/tutorials/images/
- W3C, Understanding Images of Text  
  https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html
- W3C, Understanding Use of Color  
  https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- W3C, Understanding Non-text Contrast  
  https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html
- W3C, Technique G207 for Icon Contrast  
  https://www.w3.org/WAI/WCAG21/Techniques/general/G207

### Usability evidence

- Baymard, B2B Electronic Components & Machinery  
  https://baymard.com/research/b2b-electronic-components-machinery
- Baymard, Product Page UX  
  https://baymard.com/research/product-page
- Baymard, Product Listing Information  
  https://baymard.com/blog/product-listing-information
- Baymard, Product Descriptions  
  https://baymard.com/blog/product-descriptions
- Baymard, Product Tables for Desktop B2B Listings  
  https://baymard.com/blog/use-product-tables-for-desktop-product-listings

### Performance and implementation

- web.dev, Responsive Images  
  https://web.dev/articles/responsive-images
- web.dev, Image Performance  
  https://web.dev/learn/performance/image-performance
- web.dev, Optimize Cumulative Layout Shift  
  https://web.dev/articles/optimize-cls

## D. Domain-review requirements

The following cannot be validated by general design research alone:

- correct PPE and safe work;
- accurate product configuration;
- official safety marks;
- engineering drawing conventions;
- performance curves;
- test conditions;
- standards and approvals;
- certification scope;
- simulation versus measured data.

These assets require review by qualified internal or external subject-matter experts.

## E. Visual research checklist

- [ ] Every image supports a concrete evaluation question.
- [ ] Product imagery identifies the actual model/configuration.
- [ ] Technical assets show revision and source where applicable.
- [ ] Safety and PPE received expert review.
- [ ] Meaningful graphics have accessible equivalents.
- [ ] Text is not unnecessarily baked into raster images.
- [ ] Diagram and icon contrast was tested.
- [ ] Mobile crops preserve technical meaning.
- [ ] 3D/video has a static fallback.
- [ ] Generated imagery is not presented as real evidence.
