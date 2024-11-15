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
	<div class="relative hidden h-full flex-col p-10 text-white lg:flex dark:border-r">
		<div class="absolute inset-0 bg-[url('/assets/images/auth.png')] bg-cover bg-center"></div>

		<div class="relative flex items-center gap-2">
			<img class="h-10 w-10" src="/assets/icons/devguard.svg" alt="DevGuard Agent" />

			<span class="relative block text-xl font-medium text-[#CAD1E9]">DevGuard Agent</span>
		</div>

		<div class="relative mt-auto">
			<blockquote class="space-y-2">
				<p class="text-lg">
					&ldquo;DevGuard scans your code for vulnerabilities, detects data leaks, and ensures your
					systems are ready to withstand emerging threats.&rdquo;
				</p>
				<footer>DevGuard Agent</footer>
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
