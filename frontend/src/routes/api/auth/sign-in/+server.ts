import { json } from '@sveltejs/kit';

export async function POST({ locals: { supabase }, request }) {
	const values: Record<string, string> = await request.json();
	const errors: Record<string, string> = {};

	Object.entries(values).forEach(([key, value]) => {
		if (!value.trim()) {
			errors[key as keyof typeof values] = 'This field is required.';
		}
	});

	if (Object.values(errors).some((error) => error)) {
		return json(errors, { status: 400 });
	}

	const { data, error } = await supabase.auth.signInWithPassword({
		email: values.email,
		password: values.password
	});

	if (error) {
		switch (error.code) {
			case 'invalid_credentials': {
				errors.toast = 'Invalid credentials.';
				break;
			}
			default: {
				errors.toast = 'An unexpected error occurred. Please try again later.';
			}
		}

		return json(errors, { status: error.status });
	}

	return json(data);
}
