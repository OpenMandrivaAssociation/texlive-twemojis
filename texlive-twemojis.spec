Name:		texlive-twemojis
Version:	62930
Release:	2
Summary:	Use Twitter's open source emojis through LaTeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/twemojis
License:	lppl1.3 cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twemojis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twemojis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twemojis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple wrapper which allows to use
Twitter's open source emojis through LaTeX commands. This
relies on images, so no fancy unicode-font stuff is needed and
it should work on every installation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/twemojis
%{_texmfdistdir}/tex/latex/twemojis
%doc %{_texmfdistdir}/doc/latex/twemojis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
