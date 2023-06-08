host ?= 0.0.0.0
port ?= 3000

run:
	npx vercel dev --listen $(host):$(port)
