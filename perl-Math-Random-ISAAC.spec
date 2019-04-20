#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Random-ISAAC
Version  : 1.004
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-1.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-1.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-random-isaac-perl/libmath-random-isaac-perl_1.004-1.debian.tar.xz
Summary  : 'Perl interface to the ISAAC PRNG algorithm'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0 GPL-3.0 MIT
Requires: perl-Math-Random-ISAAC-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::NoWarnings)

%description
This archive contains the distribution Math-Random-ISAAC,
version 1.004:
Perl interface to the ISAAC PRNG algorithm

%package dev
Summary: dev components for the perl-Math-Random-ISAAC package.
Group: Development
Provides: perl-Math-Random-ISAAC-devel = %{version}-%{release}

%description dev
dev components for the perl-Math-Random-ISAAC package.


%package license
Summary: license components for the perl-Math-Random-ISAAC package.
Group: Default

%description license
license components for the perl-Math-Random-ISAAC package.


%prep
%setup -q -n Math-Random-ISAAC-1.004
cd ..
%setup -q -T -D -n Math-Random-ISAAC-1.004 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Math-Random-ISAAC-1.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Random-ISAAC
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Math-Random-ISAAC/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Random-ISAAC/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Math/Random/ISAAC.pm
/usr/lib/perl5/vendor_perl/5.28.2/Math/Random/ISAAC/PP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Random::ISAAC.3
/usr/share/man/man3/Math::Random::ISAAC::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Random-ISAAC/LICENSE
/usr/share/package-licenses/perl-Math-Random-ISAAC/deblicense_copyright
