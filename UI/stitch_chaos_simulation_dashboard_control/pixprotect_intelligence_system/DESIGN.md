---
name: PixProtect Intelligence System
colors:
  surface: '#f9f9ff'
  surface-dim: '#d3daea'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eefe'
  surface-container-high: '#e2e8f8'
  surface-container-highest: '#dce2f3'
  on-surface: '#151c27'
  on-surface-variant: '#434655'
  inverse-surface: '#2a313d'
  inverse-on-surface: '#ebf1ff'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#575e70'
  on-secondary: '#ffffff'
  secondary-container: '#d9dff5'
  on-secondary-container: '#5c6274'
  tertiary: '#006242'
  on-tertiary: '#ffffff'
  tertiary-container: '#007d55'
  on-tertiary-container: '#bdffdb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#dce2f7'
  secondary-fixed-dim: '#c0c6db'
  on-secondary-fixed: '#141b2b'
  on-secondary-fixed-variant: '#404758'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#f9f9ff'
  on-background: '#151c27'
  surface-variant: '#dce2f3'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: 2.5rem
    letterSpacing: -0.025em
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '700'
    lineHeight: 2rem
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 1.25rem
    fontWeight: '600'
    lineHeight: 1.75rem
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.5rem
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.5rem
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.25rem
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '400'
    lineHeight: 1rem
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: 1.25rem
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
    letterSpacing: 0.02em
  code-mono:
    fontFamily: Inter
    fontSize: 0.8125rem
    fontWeight: '500'
    lineHeight: 1.125rem
    letterSpacing: 0em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 1.5rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system embodies a modern, corporate SaaS aesthetic tailored specifically for high-velocity fraud prevention and real-time transaction monitoring. The emotional imperative is unwavering reliability, razor-sharp precision, and analytical calm under pressure. Analysts, compliance officers, and risk managers interact with high-density data where cognitive fatigue is a direct liability; the interface therefore stays out of the way, prioritizing data legibility, swift visual scanning, and unmistakable status comprehension.

The aesthetic blends structural minimalism with corporate financial rigor:
- **Tone:** Methodical, secure, dependable, and objective.
- **Visual Weight:** Ultra-clean surfaces with disciplined contrast ratios, rejecting ornamental flair or distracting gradients in favor of structured data displays and status clarity.
- **Core Visual Drivers:** Muted canvas foundations, stark white content containers, crisp neutral dividers, and a hyper-targeted semantic palette designed for immediate risk triage (low, medium, high).

## Colors

The color architecture is built around functional hierarchy and unambiguous semantic feedback:

### Foundations & Neutrals
- **App Canvas (`#F7F8FA`):** A cool-toned, soft neutral ground that reduces glare and provides subtle separation from foreground cards.
- **Surface / Card (`#FFFFFF`):** High-purity white used for analytical cards, modal windows, table rows, and floating panels.
- **Border Default (`#E5E7EB`):** Subtle, non-intrusive container edges and table dividers ensuring clean division without visual clutter.
- **Border Muted (`#F3F4F6`):** Secondary dividers, inner cell borders, and skeleton loaders.
- **Text Primary (`#111827`):** Deep slate-black delivering maximum contrast for critical data values, transaction identifiers, and metric readouts.
- **Text Secondary (`#6B7280`):** Balanced neutral for column headers, metadata, timestamps, and secondary captions.
- **Text Muted (`#9CA3AF`):** Input placeholders, disabled states, and inactive tab indicators.

### Action & Identification
- **Primary Action (`#2563EB`):** High-clarity blue reserved strictly for interactive triggers, primary calls-to-action, active selection rings, and navigation active states.
- **Primary Hover (`#1D4ED8`):** Deepened blue for sustained interactive feedback.
- **Primary Surface (`#EFF6FF`):** Faint blue tint for active table rows, filter chips in selection state, and highlighted navigation items.

### Risk & Semantic Palette
Risk indicators must always couple color with structural textual labels to preserve accessibility:
- **Low Risk / Safe (`#10B981`):** Cleared transactions, authenticated devices, regular velocity.
  - Background tint: `#ECFDF5` | Text/Icon: `#065F46`
- **Medium Risk / Warning (`#F59E0B`):** Suspicious velocity, unfamiliar IP, step-up verification needed.
  - Background tint: `#FFFBEB` | Text/Icon: `#92400E`
- **High Risk / Critical (`#EF4444`):** Confirmed mule accounts, anomalous chargebacks, immediate hold triggers.
  - Background tint: `#FEF2F2` | Text/Icon: `#991B1B`
- **Informational Neutral (`#3B82F6`):** Standard system notices, read-only operational telemetry.

## Typography

Inter serves as the single font family across the entire hierarchy, leveraging its tall x-height, neutral letterforms, and robust open-source OpenType features:
- **Tabular Figures (`tnum`):** Enforce `font-feature-settings: 'tnum'` across all financial values, PIX End-to-End IDs, timestamps, and confidence percentages to ensure vertical tabular alignment in dense grids.
- **Case Sensitivity:** Avoid forced all-caps across long strings; reserve uppercase strictly for badge status codes (e.g., `PIX-REC`, `HOLD`, `AUTH`).
- **Hierarchy Rules:** 
  - Section headers utilize `headline-lg` with tight tracking (`-0.02em`) to maintain editorial authority without consuming valuable screen real estate.
  - Core data cells, inputs, and form controls lean strictly on `body-md` and `label-md` for maximum density and scannability.
  - Micro-metadata (device fingerprints, risk scoring formulas) uses `body-sm` in `text-secondary` (`#6B7280`).

## Layout & Spacing

The dashboard relies on a strict 8-point spatial rhythm with 24px (`1.5rem`) serving as the master structural spacing token for margins, gutters, and card separation.

### Grid & Canvas Structure
- **Desktop (1024px+):** Fixed collapsible navigation sidebar (260px expanded / 72px collapsed) paired with a 12-column fluid grid. Column gutters and card margins stay constant at `24px` (`1.5rem`).
- **Tablet (768px - 1023px):** 8-column layout with `16px` gutters. Sidebar shifts to overlay drawer.
- **Mobile (< 768px):** 4-column single-stack layout with `16px` outer gutters. High-density transaction tables collapse into structured cards.

### Spacing Application
- **`space-xs` (4px):** Gaps between icon and inline text, badge inner padding.
- **`space-sm` (8px):** Internal element spacing within form groups, table cell vertical padding, icon-to-label offset.
- **`space-md` (16px):** Padding inside compact cards, table cell horizontal padding, filter bar spacing.
- **`space-lg` (24px):** Core padding for primary operational cards, grid gap between analytical modules, and section spacing.
- **`space-xl` (32px):** Major vertical offsets between unrelated workspace sections.

## Elevation & Depth

Visual hierarchy uses a refined hybrid approach: low-contrast structural outlines combined with ambient micro-shadows (`shadow-sm`). High elevation and heavy dropshadows are forbidden to prevent muddy visuals in data-dense tables.

### Depth Levels
- **Canvas Base (Level 0):** `#F7F8FA`. Flat background, no shadow, no border.
- **Surface Container (Level 1):** `#FFFFFF` cards, metrics, and data tables. Outlined with a continuous 1px border (`#E5E7EB`) and paired with an ambient micro-shadow: `0 1px 2px 0 rgba(0, 0, 0, 0.05)`.
- **Raised Interactive (Level 2):** Hovered cards, active dropdown menus, context popovers. Outlined with 1px `#E5E7EB` and elevated with `0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05)`.
- **Overlay / Modal (Level 3):** Transaction manual review overlays and drawer panels. Outlined with 1px `#D1D5DB` and elevated with `0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.04)`. Supported by a neutral backdrop blur (`rgba(17, 24, 39, 0.4)` with `backdrop-filter: blur(2px)`).

## Shapes

The interface implements a cohesive 8px (`0.5rem`) corner radius across all core elements (`rounded-lg`), delivering a contemporary, approachable enterprise silhouette while preserving structural grid alignment.

### Radius Assignments
- **Micro Radii (`4px` / `0.25rem`):** Badges, tag chips, checkboxes, sub-elements.
- **Standard Control Radii (`8px` / `0.5rem`):** Action buttons, input controls, select pickers, metric summary tiles, and main card containers.
- **Elevated Modals (`12px` / `0.75rem`):** Centered modal dialogues and flyout drawers to soften screen interruption.
- **Circular (`9999px`):** User avatars, status pulse pips, and risk indicator score gauges.

## Components

### Buttons
- **Primary:** Background `#2563EB`, text `#FFFFFF`, border none, radius `8px`, height `38px`, font `label-md`. Hover: `#1D4ED8`. Active: `#1E40AF`. Focus: 2px offset ring in `#93C5FD`.
- **Secondary / Outline:** Background `#FFFFFF`, border 1px solid `#E5E7EB`, text `#111827`. Hover: `#F9FAFB` with border `#D1D5DB`.
- **Destructive (Block Transaction / Add to Blocklist):** Background `#FEF2F2`, border 1px solid `#FCA5A5`, text `#DC2626`. Hover: `#EF4444`, text `#FFFFFF`.

### Cards & Metrics
- Surface `#FFFFFF`, border 1px solid `#E5E7EB`, radius `8px`, ambient shadow `0 1px 2px 0 rgba(0, 0, 0, 0.05)`, padding `24px`.
- Metric tiles display the KPI title in `body-sm` (`#6B7280`), followed by a bold value in `headline-lg` (`#111827`), paired with an inline contextual pill showing delta or anomaly percentage.

### Risk Chips & Badges
- **Low Risk Pill:** Background `#ECFDF5`, text `#065F46`, border 1px solid `#A7F3D0`, font `label-sm`, padding `2px 8px`, radius `4px`.
- **Medium Risk Pill:** Background `#FFFBEB`, text `#92400E`, border 1px solid `#FDE68A`, font `label-sm`, padding `2px 8px`, radius `4px`.
- **High Risk Pill:** Background `#FEF2F2`, text `#991B1B`, border 1px solid `#FECACA`, font `label-sm`, padding `2px 8px`, radius `4px`.
- Every badge includes a 6px circular status dot on the left.

### Form Inputs & Search Fields
- Background `#FFFFFF`, border 1px solid `#E5E7EB`, radius `8px`, height `38px`, text `#111827`, placeholder `#9CA3AF`, padding `8px 12px`.
- Focus state: Border color `#2563EB` with an ambient glow outline: `box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15)`.

### Checkboxes & Radios
- Size `16px × 16px`, radius `4px` (checkbox) / `9999px` (radio).
- Default: Border 1px solid `#D1D5DB`, background `#FFFFFF`.
- Checked: Background `#2563EB`, border color `#2563EB`, checkmark glyph in `#FFFFFF`.

### Data Tables (Transaction Feed)
- **Container:** Wrapped in Level 1 card structure with overflow-x handling.
- **Header:** Background `#F9FAFB`, border-bottom 1px solid `#E5E7EB`, text `label-sm` in `#6B7280`, uppercase, padding `12px 16px`.
- **Rows:** Background `#FFFFFF`, border-bottom 1px solid `#F3F4F6`, height `48px`, font `body-md`. Hover state triggers background `#F8FAFC`.
- All monetary values and PIX keys utilize `tabular-nums` formatting with monospaced clarity.