import { json } from '@sveltejs/kit';

export async function POST({ locals: { supabase } }) {
	const { error } = await supabase.auth.signOut();

	if (error) {
		return json(
			{ toast: 'An unexpected error occurred. Please try again later.' },
			{ status: error.status }
		);
	}

	return json(null);
}
