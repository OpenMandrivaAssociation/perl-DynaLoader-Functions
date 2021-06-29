%define modname	DynaLoader-Functions

Summary:	Perl module for deconstructed dynamic C library loading
Name:		perl-%{modname}
Version:	0.003
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/DynaLoader::Functions
Source0:	http://search.cpan.org/CPAN/authors/id/Z/ZE/ZEFRAM/DynaLoader-Functions-%{version}.tar.gz
Patch0:		DynaLoader-Functions-no-VMS.patch
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Perl module for deconstructed dynamic C library loading

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%__perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build

%check
./Build test

%install
./Build install destdir="%{buildroot}" create_packlist=0

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
