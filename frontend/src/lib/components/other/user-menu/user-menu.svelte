<script lang="ts">
	import type { User as IUser } from '@supabase/supabase-js';
	import { goto, invalidate } from '$app/navigation';
	import { setMode } from 'mode-watcher';
	import { signOut } from '$lib/controllers/auth.controller';
	import { displayGeneralErrorToast } from '$lib/scripts/toast.script';
	import { LogOut, Moon, Settings, Sun, User } from 'lucide-svelte';
	import { buttonVariants } from '$lib/components/ui/button';
	import * as Avatar from '$lib/components/ui/avatar';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';

	let { user }: { user: IUser } = $props();

	let isLoadingSignOut = $state(false);

	const profilePicture = user.user_metadata.profile_picture;
	const email = user.user_metadata.email;
	const displayName = user.user_metadata.display_name;
	const abbreviatedDisplayName = user.user_metadata.display_name
		.trim()
		.split(' ')
		.map((item: string) => item.charAt(0))
		.slice(0, 2)
		.join('');

	function handleThemeItemClick(mode: 'light' | 'dark' | 'system') {
		setMode(mode);
	}

	async function handleSignOutItemClick() {
		isLoadingSignOut = true;

		try {
			await signOut();
			await invalidate('supabase:auth');
			await goto('/chat');
		} catch {
			displayGeneralErrorToast();
		}

		isLoadingSignOut = false;
	}
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger
		class={`${buttonVariants({ variant: 'ghost', size: 'icon' })} rounded-full`}
		aria-label="Meniu de utilizator"
	>
		<Avatar.Root class="rounded-lg">
			<Avatar.Image class="rounded-none" src={profilePicture} alt={displayName} />
			<Avatar.Fallback class="rounded-none">{abbreviatedDisplayName}</Avatar.Fallback>
		</Avatar.Root>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content class="w-max" side="bottom" align="end">
		<DropdownMenu.Label class="flex items-center gap-2 px-1 py-1.5">
			<Avatar.Root class="h-8 w-8 rounded-lg">
				<Avatar.Image class="rounded-none" src={profilePicture} alt={displayName} />
				<Avatar.Fallback class="rounded-none text-xs font-medium">
					{abbreviatedDisplayName}
				</Avatar.Fallback>
			</Avatar.Root>

			<div>
				<span class="block truncate text-sm font-semibold leading-tight">
					{displayName}
				</span>
				<span class="block truncate text-xs font-normal leading-tight">
					{email}
				</span>
			</div>
		</DropdownMenu.Label>
		<DropdownMenu.Separator />
		<DropdownMenu.Group>
			<DropdownMenu.Item>
				<User class="mr-2 h-4 w-4" />
				<span>Profile</span>
			</DropdownMenu.Item>
			<DropdownMenu.Item>
				<Settings class="mr-2 h-4 w-4" />
				<span>Settings</span>
			</DropdownMenu.Item>
			<DropdownMenu.Separator />
			<DropdownMenu.Sub>
				<DropdownMenu.SubTrigger>
					<Sun
						class="mr-2 h-4 w-4 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
					/>
					<Moon
						class="absolute mr-2 h-4 w-4 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
					/>
					<span>Theme</span>
				</DropdownMenu.SubTrigger>
				<DropdownMenu.SubContent>
					<DropdownMenu.Item onclick={() => handleThemeItemClick('light')}>Light</DropdownMenu.Item>
					<DropdownMenu.Item onclick={() => handleThemeItemClick('dark')}>Dark</DropdownMenu.Item>
					<DropdownMenu.Item onclick={() => handleThemeItemClick('system')}>
						System
					</DropdownMenu.Item>
				</DropdownMenu.SubContent>
			</DropdownMenu.Sub>
		</DropdownMenu.Group>
		<DropdownMenu.Separator />
		<DropdownMenu.Item disabled={isLoadingSignOut} onclick={handleSignOutItemClick}>
			<LogOut class="mr-2 h-4 w-4" />
			<span>Log out</span>
		</DropdownMenu.Item>
	</DropdownMenu.Content>
</DropdownMenu.Root>
