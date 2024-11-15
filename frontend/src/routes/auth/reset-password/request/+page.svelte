<script lang="ts">
	import { sendPasswordResetEmail } from '$lib/controllers/auth.controller';
	import {
		displayErrorToast,
		displayGeneralErrorToast,
		displaySuccessToast
	} from '$lib/scripts/toast.script';
	import { validateEmail } from '$lib/scripts/validation.script';
	import { Loader2 } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import { InputText } from '$lib/components/form/input-text';

	let values = $state({ email: '' });
	let errors = $state({ email: '' });
	let isLoading = $state(false);

	async function handleSubmit(event: SubmitEvent) {
		event.preventDefault();

		Object.entries(values).forEach(([key, value]) => {
			if (!value.trim()) {
				errors[key as keyof typeof values] = 'This field is required.';
			}
		});

		if (values.email && !validateEmail(values.email)) {
			errors.email = 'Please enter a valid email address.';
		}

		if (Object.values(errors).some((error) => error)) {
			return;
		}

		isLoading = true;

		try {
			await sendPasswordResetEmail(values.email);
			displaySuccessToast(
				'If the email address you entered is associated with an account, you will soon receive a password reset email. If you cannot find the email, please also check your spam or junk folder.'
			);
		} catch (error) {
			handleError(error);
		}

		isLoading = false;
	}

	function handleError(error: any) {
		if (Object.entries(error).length) {
			Object.entries(error).forEach(([key, value]) => {
				if (key in errors) {
					errors[key as keyof typeof errors] = value as string;
				} else {
					displayErrorToast(error[key]);
				}
			});
		} else {
			displayGeneralErrorToast();
		}
	}
</script>

<svelte:head>
	<title>Reset password</title>
</svelte:head>

<div class="grow space-y-6">
	<div class="space-y-1.5">
		<h1 class="text-2xl font-semibold tracking-tight lg:text-3xl">Reset password</h1>
		<p class="text-muted-foreground text-sm lg:text-base">
			Enter your email address in the field below and we'll send you instructions to reset password.
		</p>
	</div>

	<form class="space-y-6" onsubmit={handleSubmit}>
		<div class="space-y-4">
			<InputText
				id="email"
				label="Email address"
				placeholder="Enter your email address"
				bind:value={values.email}
				bind:error={errors.email}
			/>
		</div>

		<Button class="w-full" type="submit" disabled={isLoading}>
			{#if isLoading}
				<Loader2 class="!h-5 !w-5 animate-spin" />
			{/if}

			<span>Continue</span>
		</Button>
	</form>
</div>
