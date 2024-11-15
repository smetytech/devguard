<script lang="ts">
	import { goto, invalidate } from '$app/navigation';
	import { signIn } from '$lib/controllers/auth.controller';
	import { displayErrorToast, displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import { validateEmail } from '$lib/scripts/validation.script';
	import { Loader2 } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import { InputPassword } from '$lib/components/form/input-password';
	import { InputText } from '$lib/components/form/input-text';

	let values = $state({ email: '', password: '' });
	let errors = $state({ email: '', password: '' });
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
			await signIn(values.email, values.password);
			await invalidate('supabase:auth');
			await goto('/');
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
	<title>Sign In</title>
</svelte:head>

<div class="grow space-y-6">
	<div class="space-y-1.5">
		<h1 class="text-2xl font-semibold tracking-tight lg:text-3xl">Sign In</h1>
		<p class="text-muted-foreground text-sm lg:text-base">Fill in the form below to log in.</p>
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

			<InputPassword
				id="password"
				label="Password"
				placeholder="Enter your account password"
				bind:value={values.password}
				bind:error={errors.password}
			/>
		</div>

		<div class="space-y-3">
			<Button class="w-full" type="submit" disabled={isLoading}>
				{#if isLoading}
					<Loader2 class="!h-5 !w-5 animate-spin" />
				{/if}

				<span>Continue</span>
			</Button>

			<Button class="w-full" variant="link" href="/auth/reset-password/request">
				<span>Forgot password?</span>
			</Button>
		</div>
	</form>
</div>
