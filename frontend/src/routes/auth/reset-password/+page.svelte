<script lang="ts">
	import { goto } from '$app/navigation';
	import { resetPassword } from '$lib/controllers/auth.controller';
	import {
		displayErrorToast,
		displayGeneralErrorToast,
		displaySuccessToast
	} from '$lib/scripts/toast.script';
	import { validatePassword } from '$lib/scripts/validation.script';
	import { Loader2 } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import { InputPassword } from '$lib/components/form/input-password';

	let values = $state({ password: '', confirmPassword: '' });
	let errors = $state({ password: '', confirmPassword: '' });
	let isLoading = $state(false);

	async function handleSubmit(event: Event) {
		event.preventDefault();

		Object.entries(values).forEach(([key, value]) => {
			if (!value.trim()) {
				errors[key as keyof typeof values] = 'This field is required.';
			}
		});

		if (values.password && !validatePassword(values.password)) {
			errors.password =
				'The password must be at least 8 characters long and contain an uppercase letter, a lowercase letter, a digit and a special character.';
		}

		if (values.password && values.confirmPassword && values.password !== values.confirmPassword) {
			errors.confirmPassword = 'The passwords you entered do not match.';
		}

		if (Object.values(errors).some((error) => error)) {
			return;
		}

		isLoading = true;

		try {
			await resetPassword(values.password);
			await goto('/auth/sign-in');

			displaySuccessToast(
				'Your account password has been reset. Please log in to access your account.'
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
			Fill in the form below to reset your account password.
		</p>
	</div>

	<form class="space-y-6" onsubmit={handleSubmit}>
		<div class="space-y-4">
			<InputPassword
				id="password"
				label="Password"
				placeholder="Choose a secure password"
				bind:value={values.password}
				bind:error={errors.password}
			/>

			<InputPassword
				id="confirm-password"
				label="Confirm password"
				placeholder="Confirm your password"
				bind:value={values.confirmPassword}
				bind:error={errors.confirmPassword}
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
