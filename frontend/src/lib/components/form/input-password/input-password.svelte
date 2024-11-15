<script lang="ts">
	import { Eye, EyeOff } from 'lucide-svelte';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';

	let {
		id,
		label,
		placeholder,
		value = $bindable(),
		error = $bindable()
	}: {
		id: string;
		label: string | undefined;
		placeholder: string | undefined;
		value: string | undefined;
		error: string | undefined;
	} = $props();

	let type = $state('password');

	function handleVisibilityButtonClick() {
		if (type === 'password') {
			type = 'text';
		} else {
			type = 'password';
		}
	}

	function handleInput() {
		error = '';
	}
</script>

<div class="flex flex-col gap-1.5">
	{#if label}
		<Label class={error && 'text-destructive'} for={id}>{label}</Label>
	{/if}

	<div class="relative">
		<Input
			class="{error && 'border-destructive !ring-destructive'} truncate"
			{id}
			{type}
			{placeholder}
			bind:value
			oninput={handleInput}
		/>

		{#if value}
			<button
				class="absolute right-2 top-1/2 -translate-y-1/2 p-1"
				type="button"
				onclick={handleVisibilityButtonClick}
			>
				{#if type === 'password'}
					<Eye class="h-4 w-4" />
				{:else}
					<EyeOff class="h-4 w-4" />
				{/if}
			</button>
		{/if}
	</div>

	{#if error}
		<span class="text-destructive text-[0.8rem]">{error}</span>
	{/if}
</div>
