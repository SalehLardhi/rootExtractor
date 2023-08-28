import argparse
import sys

def get_root_domain(subdomain):
	parts = subdomain.split('.')
	if len(parts) < 2:
		return None
	if len(parts) == 2:
		return parts[1]
	else:
		return '.'.join(parts[-2:])

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--list', required=True, help='Input file containing a list of subdomains')
	parser.add_argument('-o', '--output', required=True, help='Output file to write root domains to')
	args = parser.parse_args()

	with open(args.list, 'r') as f:
		subdomains = f.read().splitlines()

	with open(args.output, 'w') as f:
		for subdomain in subdomains:
			root_domain = get_root_domain(subdomain)
			if root_domain:
				f.write(root_domain + '\n')

if __name__ == '__main__':
	main()