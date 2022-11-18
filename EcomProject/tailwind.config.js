/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./pages/**/*.{html,js}",
  "./node_modules/flowbite/**/*.{ts,js,d}"
  ,'./node_modules/tw-elements/dist/js/**/*.js'],
  theme: {
    extend: {},
  },
  plugins: [require('flowbite/plugin'),require('tw-elements/dist/plugin') ],
}
