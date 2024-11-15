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

	const { data, error } = await supabase.auth.signUp({
		email: values.email,
		password: values.password,
		options: {
			data: {
				display_name: values.name,
				role: 'USER'
			}
		}
	});

	if (error) {
		switch (error.code) {
			case 'weak_password': {
				errors.password =
					'The password must be at least 8 characters long and contain an uppercase letter, a lowercase letter, a digit and a special character.';
				break;
			}
			case 'user_already_exists': {
				errors.toast = 'The email address entered is already associated with an account.';
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
