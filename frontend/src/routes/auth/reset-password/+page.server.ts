import { error } from '@sveltejs/kit';

export async function load({ url }) {
	const errorCode = url.searchParams.get('error_code');
	const errorDescription = url.searchParams.get('error_description');

	if (errorCode && errorDescription) {
		throw error(parseInt(errorCode), errorDescription);
	}
}
