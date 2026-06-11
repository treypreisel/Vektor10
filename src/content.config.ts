import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Blog posts are plain markdown in src/content/blog — one file per post.
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    author: z.string().default('Todd Piechowski'),
    role: z.string().default('Founder & CEO, Vektor10'),
    readTime: z.string().default('5 min read'),
    canonical: z.string().url().optional(),
  }),
});

export const collections = { blog };
