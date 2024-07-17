/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'mulish': ['"Mulish"', 'sans-serif'],
        'robotoCondensed': ['"Roboto Condensed"', 'sans-serif']
      },
      colors: {
        'my-blue': '#083C5A',
        'my-yellow': '#FCC72C',
        'my-green': '#4CB648',
        'my-soft-blue': '#E4F4FD'
      }
    },
  },
  plugins: [],
};
