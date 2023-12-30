import type { Config } from 'tailwindcss'
import daisyui from 'daisyui';

export default {
  content: ['./index.html', './src/pages/**/*.{ts,tsx}', './src/components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [daisyui],
  daisyui: {
    themes: ["winter", "night"]
  }
} as Config

