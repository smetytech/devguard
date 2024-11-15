import { json } from '@sveltejs/kit';

export async function POST({ locals: { supabase }, request, url }) {
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

	const { data, error } = await supabase.auth.resetPasswordForEmail(values.email, {
		redirectTo: `${url.origin}/auth/reset-password`
	});

	if (error) {
		switch (error.code) {
			case 'over_email_send_rate_limit': {
				errors.toast =
					'You have reached the maximum number of password reset attempts. Please try again later.';
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
