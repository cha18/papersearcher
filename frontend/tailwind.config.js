/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        spacemono: ['Space Mono', 'sans-serif'],
        dmserif: ['DM Serif Text', 'serif']
      },
    },
  },
  plugins: [],
}

