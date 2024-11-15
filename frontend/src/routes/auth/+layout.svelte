<script lang="ts">
	import { page } from '$app/stores';
	import { ArrowLeft } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button';

	let { children } = $props();

	let isSignUpRoute = $derived($page.route.id === '/auth/sign-up');
	let isSignInRoute = $derived($page.route.id === '/auth/sign-in');

	function handleBackButtonClick() {
		history.back();
	}
</script>

<div class="relative grid h-screen lg:grid-cols-2">
	<div class="bg-muted relative hidden h-full flex-col p-10 text-white lg:flex dark:border-r">
		<div
			class="absolute inset-0 bg-[url(https://images.unsplash.com/photo-1590069261209-f8e9b8642343?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1376&q=80)] bg-cover"
		></div>

		<span class="relative block text-lg font-medium">DevGuard</span>
		<div class="relative mt-auto">
			<blockquote class="space-y-2">
				<p>
					&ldquo;This library has saved me countless hours of work and helped me deliver stunning
					designs to my clients faster than ever before. Highly recommended!&rdquo;
				</p>
				<footer class="text-sm">Mihnea Huțuțui</footer>
			</blockquote>
		</div>
	</div>

	<div class="relative h-full p-4 lg:p-8">
		<div class="absolute inset-x-4 top-4 flex items-center justify-between lg:inset-x-8 lg:top-8">
			<Button variant="ghost" onclick={handleBackButtonClick}>
				<ArrowLeft class="!h-5 !w-5" />
				<span>Back</span>
			</Button>

			{#if isSignUpRoute}
				<Button variant="ghost" href="/auth/sign-in">
					<span>Sign In</span>
				</Button>
			{:else if isSignInRoute}
				<Button variant="ghost" href="/auth/sign-up">
					<span>Sign Up</span>
				</Button>
			{/if}
		</div>

		<div class="mx-auto flex h-full w-full max-w-96 items-center justify-center px-2 py-14 lg:px-0">
			{@render children()}
		</div>
	</div>
</div>
