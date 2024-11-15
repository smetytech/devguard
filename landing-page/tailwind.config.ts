import { fontFamily } from 'tailwindcss/defaultTheme';
import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				background: '#050520',
				foreground: '#cad1e9'
			},
			fontFamily: {
				sans: ['Inter', ...fontFamily.sans],
				rubik: ['Rubik', ...fontFamily.sans],
				roboto: ['Roboto', ...fontFamily.sans]
			}
		}
	},
	plugins: []
} as Config;
