import type { Session, SupabaseClient, User } from '@supabase/supabase-js';

declare global {
	namespace App {
		interface Locals {
			safeGetSession: () => Promise<{ session: Session | null; user: User | null }>;
			supabase: SupabaseClient;
			session: Session | null;
			user: User | null;
		}
		interface PageData {
			session: Session | null;
		}
	}
}

export {};
