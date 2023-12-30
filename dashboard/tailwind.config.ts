import type { Config } from 'tailwindcss'
import daisyui from 'daisyui';

export default {
  content: ["./src/**/*.{ts,tsx, html}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [
    daisyui
  ],
  daisyui: {
    themes: ["acid", "winter"]
  }
} satisfies Config

