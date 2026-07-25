# Immersive Storytelling Images & Graphic Assets Guide 2026

> A comprehensive, brand-neutral guide for photography, video, audio, illustration, 3D, WebGL, maps, data scenes, icons, borders, separators, motion assets, and responsive production in immersive narrative websites.
>
> Use this document together with `immersive-storytelling-web-design-system-2026.md`.

---

## 1. Purpose

Immersive visual assets should create narrative understanding, spatial presence, emotional context, or evidence.

Every asset must have a clear role:

```text
Evidence
Narrative explanation
Navigation
Atmosphere
```

Priority:

```text
Evidence > narrative explanation > navigation > atmosphere
```

An atmospheric asset should not obscure the factual or navigational layer.

---

## 2. Visual direction

Suitable directions include:

- cinematic documentary;
- illustrated world;
- spatial 3D;
- archival narrative;
- data-led;
- environmental;
- product journey;
- tactile mixed media;
- typographic narrative;
- map-based exploration.

Choose one primary direction and limited supporting languages.

Example:

```text
Primary: Cinematic documentary
Supporting: Annotated maps and restrained data graphics
Avoid: Generic 3D particles, unrelated stock video, decorative WebGL
```

---

## 3. Asset plan by chapter

For every chapter, define:

```text
Primary message
Primary asset
Supporting asset
Caption/source
Interaction
Entry state
Active state
Exit state
Mobile asset
Reduced-motion asset
Fallback asset
Performance weight
Rights
```

This prevents the project from becoming a collection of unrelated media.

---

## 4. Photography

Photography may establish:

- person;
- place;
- time;
- evidence;
- emotion;
- scale;
- process;
- transition.

Create sequences rather than isolated images.

A documentary sequence may include:

1. establishing view;
2. medium context;
3. action;
4. person;
5. detail;
6. evidence;
7. transition;
8. outcome.

---

## 5. Photography composition

Plan for narrative state.

Specify:

- subject position;
- camera movement;
- image sequence;
- crop transition;
- negative space;
- text-safe area;
- aspect ratio;
- mobile crop;
- zoom limits;
- caption position.

Do not rely on arbitrary cropping during development.

---

## 6. Image sequences

Image sequences can simulate:

- motion;
- rotation;
- time;
- assembly;
- transformation;
- comparison.

Rules:

- use only enough frames to communicate;
- preload carefully;
- compress;
- provide final-state fallback;
- avoid large sequences on mobile;
- ensure scroll remains responsive;
- do not require all frames for basic understanding.

---

## 7. Video roles

### Documentary video

Provides factual evidence and context.

### Narrative video

Advances story through sequence and editing.

### Background video

Creates atmosphere but should not carry essential information.

### Interview

Provides voice and expertise.

### Process video

Explains operation or transformation.

### Transition video

Connects chapters.

Label reenactment, reconstruction, simulation, or generated video clearly.

---

## 8. Video production

Plan:

```text
Resolution
Frame rate
Duration
Codec
Poster
Audio
Captions
Transcript
Loop
Controls
Mobile version
Reduced-motion fallback
Preload
Rights
```

Keep loops seamless only where repetition is appropriate.

Avoid long ambient footage with little narrative value.

---

## 9. Video delivery

Use:

- poster images;
- several resolutions;
- appropriate codecs;
- preload metadata or none where suitable;
- muted autoplay only when justified;
- user-initiated audio;
- lazy loading;
- visible controls;
- captions.

Do not download large background video before essential content.

---

## 10. Audio

Audio assets may include:

- narration;
- interview;
- ambient sound;
- music;
- effects;
- spatial sound.

Requirements:

- explicit start;
- visible mute;
- volume;
- transcript;
- captioning for meaningful sound;
- no essential audio-only information;
- respect user preference;
- avoid overlapping sources.

Use emotional sound carefully in journalism, health, policy, or sensitive stories.

---

## 11. Illustration

Illustration may create a world or explain something that cannot be photographed.

Suitable directions:

- cinematic painted;
- editorial;
- technical;
- collage;
- hand-drawn;
- isometric;
- surreal;
- cut-paper;
- animated linework;
- map illustration.

Define:

```text
Stroke
Fill
Palette
Perspective
Texture
Animation style
Depth
Detail level
Character system
```

Do not mix several incompatible illustration worlds.

---

## 12. Layered illustration

Layered illustration may support parallax and spatial depth.

Create layers by real narrative plane:

```text
Background environment
Midground context
Primary subject
Foreground detail
Annotation
Atmosphere
```

Avoid splitting a flat image into many arbitrary layers only to create motion.

Keep movement differences small enough to avoid discomfort.

---

## 13. 3D assets

3D may represent:

- product;
- architecture;
- anatomy;
- landscape;
- data;
- artifact;
- system;
- historical reconstruction.

Define:

```text
Polygon budget
Texture size
Lighting
Camera
Interaction
Initial view
Annotations
Animation
Mobile model
Static fallback
Loading state
Error state
Accuracy review
```

Compress geometry and textures.

Do not create photoreal 3D that may be mistaken for documentary evidence without labelling.

---

## 14. 3D interaction

Provide familiar controls:

- rotate;
- zoom;
- pan;
- reset;
- next view;
- hotspot list.

Do not require precision gestures.

Provide labelled alternatives to direct manipulation.

Prevent users from getting lost in empty 3D space.

---

## 15. WebGL and canvas

Use WebGL or canvas when standard HTML, CSS, SVG, or video cannot provide the required result efficiently.

Requirements:

- semantic content outside canvas;
- loading and error state;
- device capability check;
- fallback;
- reduced-motion version;
- keyboard-accessible equivalent;
- capped pixel ratio;
- pause when offscreen;
- cleanup of resources;
- battery and memory testing.

Canvas output alone is not accessible content.

---

## 16. Data scenes

A data scene should define:

- question;
- chart state;
- annotation;
- transition;
- source;
- units;
- time;
- uncertainty;
- final takeaway;
- table or text equivalent.

Stage changes sequentially.

Do not animate all data marks at once when comprehension is the goal.

---

## 17. Maps

Map assets may include:

- base map;
- labels;
- routes;
- points;
- regions;
- terrain;
- archive overlays;
- time layers.

Use a restrained basemap.

Provide:

- legend;
- current story location;
- direct labels;
- list alternative;
- static map;
- source and date.

Avoid requiring hover for important map information.

---

## 18. Timelines

Timelines may be:

- vertical;
- horizontal;
- map-linked;
- media-led;
- interactive;
- data-driven.

Each event needs:

```text
Date or period
Title
Description
Source
Media
Relationship
```

Do not compress unequal time periods without explanation.

Provide a conventional list fallback.

---

## 19. Before-and-after assets

Suitable patterns:

- side-by-side;
- slider;
- crossfade;
- aligned scroll sequence;
- layered annotation.

Rules:

- label states;
- keep viewpoint comparable;
- provide keyboard controls;
- avoid using drag as the only interaction;
- preserve both images separately;
- describe the difference.

---

## 20. Archive and historical media

Archive assets require:

- title;
- date;
- source;
- creator;
- rights;
- context;
- restoration notes;
- uncertainty;
- transcription if text is important.

Do not animate archive in ways that imply it is live footage.

Do not colorize or reconstruct without disclosure.

---

## 21. Generated and reconstructed media

Clearly label:

- AI generated;
- CGI;
- artistic reconstruction;
- reenactment;
- simulation;
- representative visualization.

Do not mix generated scenes with documentary media without visible distinction.

Internally record prompt, model/tool, date, editor, source inputs, and review.

---

## 22. Typography in scenes

Typography may function as:

- narration;
- chapter marker;
- quotation;
- caption;
- source;
- interaction cue;
- data label.

Keep long reading text stable.

Avoid text moving independently while users are trying to read.

Use live HTML for meaningful text.

---

## 23. Icons and controls

Immersive experiences require clear controls.

Common controls:

- play;
- pause;
- mute;
- volume;
- captions;
- transcript;
- reset;
- rotate;
- zoom;
- next/previous;
- chapter menu;
- skip animation;
- full screen.

Use familiar icons plus labels or tooltips.

Do not invent unusual controls for common media behavior.

---

## 24. Progress graphics

Progress may use:

- chapter list;
- timeline;
- line;
- map;
- percentage;
- numbered sequence.

The progress system should remain stable while scenes change.

Avoid progress indicators that animate continuously or obscure content.

---

## 25. Borders and frames

Frames may distinguish:

- media;
- archive;
- data;
- simulation;
- quotation;
- interactive stage.

Suitable treatments:

- cinematic letterbox;
- editorial rule;
- archive frame;
- technical border;
- soft mask;
- full-bleed edge.

Use one consistent semantic system.

Do not decorate every asset with a different frame.

---

## 26. Separators and transitions

Separators may be:

- visual cut;
- color shift;
- line;
- chapter title;
- sound transition;
- material change;
- empty pause;
- full-width still.

Use transitions to communicate a narrative boundary.

Avoid several effects at once.

---

## 27. Particles and atmosphere

Particles, fog, grain, light, weather, and abstract motion may create atmosphere.

Rules:

- keep density controlled;
- pause offscreen;
- reduce on mobile;
- remove for reduced motion;
- avoid behind body text;
- use a performance cap;
- do not simulate evidence.

Generic floating particles are not a story.

---

## 28. Motion design system

Define motion tokens:

```text
Fast feedback
Scene transition
Narrative reveal
Ambient loop
Scroll-linked range
Reduced-motion replacement
```

Document:

- duration;
- easing;
- distance;
- opacity;
- trigger;
- loop;
- cancellation;
- device adaptation.

Avoid each scene inventing its own physics.

---

## 29. Reduced-motion assets

Prepare explicit alternatives:

- static hero poster;
- final chart;
- stacked illustrations;
- still image instead of parallax;
- image gallery instead of 3D;
- full text instead of kinetic fragments;
- manual play instead of autoplay;
- discrete chapter states.

Reduced motion should not mean missing content.

---

## 30. Responsive assets

For each asset define:

```text
Desktop
Tablet
Mobile
Low bandwidth
Reduced motion
No JavaScript
Print/share
```

Mobile may require:

- alternate crop;
- simplified illustration;
- fewer layers;
- lower-resolution video;
- static 3D view;
- shorter sequence;
- text outside media;
- chapter cards.

---

## 31. Image delivery

Use modern responsive image markup.

```html
<picture>
  <source
    media="(max-width: 48rem)"
    type="image/avif"
    srcset="/media/scene-mobile-640.avif 640w,
            /media/scene-mobile-960.avif 960w"
    sizes="100vw"
  />
  <source
    type="image/avif"
    srcset="/media/scene-960.avif 960w,
            /media/scene-1440.avif 1440w,
            /media/scene-1920.avif 1920w"
    sizes="100vw"
  />
  <img
    src="/media/scene-1440.webp"
    width="1920"
    height="1080"
    alt="Specific alternative text"
    decoding="async"
  />
</picture>
```

Specify dimensions and loading priority based on scene position.

---

## 32. Accessibility

For each asset classify:

```text
Informative
Functional
Decorative
Complex
Timed media
Interactive graphic
Generated/reconstructed
```

Provide:

- alt text;
- detailed description;
- captions;
- transcript;
- audio description where appropriate;
- table or text alternative;
- keyboard control;
- visible focus;
- reduced motion;
- pause/stop/hide;
- source and status.

Decorative atmosphere should be hidden from assistive technology.

---

## 33. Performance

Track per asset:

- compressed size;
- decoded size;
- texture memory;
- polygon count;
- frame rate;
- CPU/GPU use;
- loading priority;
- cache;
- mobile fallback.

Pause or unload offscreen heavy assets where appropriate.

Avoid running several canvases or videos simultaneously.

---

## 34. Rights and provenance

Record:

- creator;
- subject;
- date;
- location;
- source;
- license;
- consent;
- archive owner;
- reconstruction status;
- AI/CGI status;
- modifications;
- caption;
- approved use;
- review date.

Immersion increases perceived realism, so provenance must be especially clear.

---

## 35. AI-generation template

```text
Clearly illustrative immersive story asset, not documentary evidence.
Story chapter: [chapter].
Primary message: [message].
Subject/environment: [specific].
Visual direction: [cinematic illustration, 3D reconstruction, collage, etc.].
Composition: layered depth with clear focal point and text-safe area.
Motion plan: [static layers / short loop / manual sequence].
Color/light: [specific].
Page role: [hero, transition, chapter stage].
Exclude: generated text, logos, false historical details, documentary appearance
without disclosure, excessive particles, illegible labels.
Aspect ratio: [ratio].
```

Verify any historical, scientific, product, or geographic details independently.

---

## 36. File naming

Examples:

```text
chapter-01-establishing-coast-wide.avif
chapter-01-establishing-mobile.avif
chapter-02-process-loop-muted.webm
chapter-03-map-routes.svg
chapter-04-product-model-compressed.glb
chapter-04-product-fallback.webp
archive-letter-1928-page-01.webp
data-emissions-final-state.svg
control-skip-animation.svg
```

---

## 37. Anti-patterns

Avoid:

- unrelated cinematic stock;
- generic particle backgrounds;
- several videos playing together;
- 3D with no fallback;
- canvas-only text;
- motion required for understanding;
- archive without source;
- CGI presented as real;
- AI video presented as documentary;
- captions treated as decoration;
- controls hidden until hover;
- tiny progress indicators;
- huge image sequences on mobile;
- parallax behind body text;
- audio without transcript;
- inaccessible before/after sliders;
- media loaded before essential content.

---

## 38. AI-agent instructions

The agent must:

1. tie each asset to a chapter message;
2. classify evidence, explanation, navigation, or atmosphere;
3. storyboard asset states;
4. define mobile, reduced-motion, and fallback versions;
5. label archive, simulation, CGI, and AI;
6. define controls and accessibility;
7. define loading and performance budgets;
8. maintain source and rights;
9. preserve live text outside canvas;
10. avoid false realism;
11. prepare static exports;
12. test on real devices;
13. ensure atmosphere remains subordinate.

---

## 39. Production checklist

### Story assets
- [ ] Chapter message
- [ ] Primary and supporting assets
- [ ] Caption and source
- [ ] Entry, active, exit states
- [ ] Mobile version
- [ ] Reduced-motion version
- [ ] Fallback

### Media
- [ ] Image crops
- [ ] Video poster and captions
- [ ] Transcript
- [ ] Audio controls
- [ ] 3D compression and fallback
- [ ] Data source
- [ ] Map/list alternative

### Controls
- [ ] Play/pause
- [ ] Mute/volume
- [ ] Captions/transcript
- [ ] Reset
- [ ] Chapter navigation
- [ ] Skip animation
- [ ] Keyboard and focus

### Performance
- [ ] Asset budget
- [ ] LCP priority
- [ ] Lazy loading
- [ ] Offscreen pause
- [ ] Frame-rate test
- [ ] Mobile memory
- [ ] Failed-media state

### Provenance
- [ ] Rights
- [ ] Consent
- [ ] Archive source
- [ ] CGI/AI label
- [ ] Reconstruction note
- [ ] Review date

---

## 40. Research basis

- W3C, Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C, Understanding Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- web.dev, Video Performance: https://web.dev/learn/performance/video-performance
- Chrome Developers, Scroll-Driven Animations: https://developer.chrome.com/blog/scroll-driven-animations-video-course
- Chrome Developers, Scroll Animation Performance: https://developer.chrome.com/blog/scroll-animation-performance-case-study
- Scrollytelling as an Alternative Format for Privacy Policies: https://arxiv.org/abs/2603.04367
- Creative Bloq, Parallax Scrolling Websites: https://www.creativebloq.com/web-design/parallax-scrolling-1131762
- Creative Bloq, Graphic Design Trends 2026: https://www.creativebloq.com/design/graphic-design/texture-warmth-and-tactile-rebellion-the-big-graphic-design-trends-for-2026

---

## 41. Final rule

Immersive visual assets must advance the story, explain evidence, orient the user, or create necessary atmosphere. Every moving or spatial asset needs a meaningful purpose, an accessible control model, and a robust static alternative.
