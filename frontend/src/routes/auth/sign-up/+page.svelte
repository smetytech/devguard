<script lang="ts">
	import { goto, invalidate } from '$app/navigation';
	import { signUp } from '$lib/controllers/auth.controller';
	import { displayErrorToast, displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import { validateEmail, validatePassword } from '$lib/scripts/validation.script';
	import { Loader2 } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';
	import { InputPassword } from '$lib/components/form/input-password';
	import { InputText } from '$lib/components/form/input-text';

	let values = $state({ name: '', email: '', password: '' });
	let errors = $state({ name: '', email: '', password: '' });
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

		if (values.password && !validatePassword(values.password)) {
			errors.password =
				'The password must be at least 8 characters long and contain an uppercase letter, a lowercase letter, a digit and a special character.';
		}

		if (Object.values(errors).some((error) => error)) {
			return;
		}

		isLoading = true;

		try {
			await signUp(values.email, values.password, values.name);
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
	<title>Sign Up</title>
</svelte:head>

<div class="grow space-y-6">
	<div class="space-y-1.5">
		<h1 class="text-2xl font-semibold tracking-tight lg:text-3xl">Sign Up</h1>
		<p class="text-muted-foreground text-sm lg:text-base">
			Fill in the form below to create a new account.
		</p>
	</div>

	<form class="space-y-6" onsubmit={handleSubmit}>
		<div class="space-y-4">
			<InputText
				id="name"
				label="Full name"
				placeholder="Enter your full name"
				bind:value={values.name}
				bind:error={errors.name}
			/>

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
				placeholder="Choose a secure password"
				bind:value={values.password}
				bind:error={errors.password}
			/>
		</div>

		<Button class="w-full" type="submit" disabled={isLoading}>
			{#if isLoading}
				<Loader2 class="!h-5 !w-5 animate-spin" />
			{/if}

			<span>Continue</span>
		</Button>
	</form>

	<p class="text-muted-foreground px-8 text-center text-sm">
		By clicking continue, you agree to our
		<a href="/terms" class="hover:text-primary underline underline-offset-4">Terms of Service</a>
		and
		<a href="/privacy" class="hover:text-primary underline underline-offset-4">Privacy Policy</a>
		&#8203;.
	</p>
</div>
