from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError

emails = input()

valid_domains = {'.com', '.bg', '.org', '.net'}
while not emails == 'End':
    if '@' not in emails:
        raise MustContainAtSymbolError("Email must contain @")
    emails = emails.split('@')
    domain_name = emails[-1]  # for domain we need only last index but if email is vicho@25_bul@abv.bg
    name = '@'.join(emails[0:-1])  # we must make name again 'vicho@25_bul' if in name have '@'

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if '.' not in domain_name:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    domain = domain_name.split('.')[-1]  # we want only domain
    domain = '.' + domain    # do this to be the same like in set for validation
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    emails = input()
